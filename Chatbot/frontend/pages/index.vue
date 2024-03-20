<script setup>
const dialog = reactive({
    text: '',
    type: '',
    name: '',
    image: '',
    historyId: null,
});

const includeDialog = ((type) => {
    if (type === 'Q') {
        dialog.image = 'user.png';
        dialog.name = 'Rhuan';
        dialog.type = 'right';
    } else {
        dialog.image = 'bot.png';
        dialog.name = 'Bot';
        dialog.type = 'left';
    }
    // faz a cópia profunda da estrutura com os valores atuais (deep copy)
    conversationHistory.value.push(
        JSON.parse(JSON.stringify(dialog))
    );
});

const Messages = async (historyId) => {
    const { data: getMessages } = await useFetch(`http://localhost:8000/chatbot/conversation/${historyId}`, {
        method: 'GET'
    })
    const history = getMessages
    for (const message of history.value) {
        dialog.text = message.message;
        dialog.historyId = message.history.id;
        includeDialog(message.type);
        dialog.text = '';
    }
}

const sendMessage = async () => {
    let historyIsNull = false
    if (dialog.historyId == null) { historyIsNull = true }
    includeDialog('Q');

    //message.value;
    const { data: answer } = await useFetch('http://localhost:8000/chatbot/', {
        method: 'POST',
        body: {
            question: dialog.text,
            userId: 2,
            conversationId: dialog.historyId
        }
    })
    dialog.text = answer.value.message;
    dialog.historyId = answer.value.history.id;
    includeDialog('A');
    dialog.text = '';
    if (historyIsNull) { userConversations() }
}

//armazena em tela o histórico das mensagens
const conversationHistory = ref([]);

const conversation = reactive({
    id: null,
    lastMessage: '',
});

const Conversations = ref([]);

const includeConversation = () => {
    // Faz a cópia profunda da estrutura com os valores atuais (deep copy)
    Conversations.value.push(
        JSON.parse(JSON.stringify(conversation))
    );
};

function limitString(str) {
    return str.length > 20 ? str.substring(0, 20) + "..." : str;
}

const userConversations = async () => {
    const { data: getConversations } = await useFetch(`http://127.0.0.1:8000/chatbot/history/`, {
        method: 'GET'
    });

    Conversations.value = [];
    for (const userConversation of getConversations.value) {
        conversation.id = userConversation.id;
        conversation.lastMessage = userConversation.id + ' - ' + limitString(userConversation.lastMessage);
        includeConversation();
        conversation.id = null;
        conversation.lastMessage = '';
    }
};

userConversations();

const selectedConversation = ref(null);

watch(selectedConversation, (newValue, oldValue) => {
    console.log(selectedConversation._value.id);
    const historyId = selectedConversation.value.id;
    conversationHistory.value = [];
    dialog.historyId = historyId;
    Messages(historyId);
})

const newChat = async () => {
    dialog.historyId = null;
    conversationHistory.value = [];
    userConversations();

}

console.log(Conversations)

</script>

<template>
    <Splitter style="height: 96vh">
        <SplitterPanel class="flex align-items-center justify-content-center" :size="25" :minSize="10">
            <div style="width: 100%; height: 10%;">
                <Button @click="newChat" label="New Chat＋" class="newChatButton" iconPos="right">
                </Button>
            </div>
            <ScrollPanel style="width: 100%; height: 90%" :pt="{
            wrapper: {
                style: { 'border-right': '10px solid var(--surface-ground)', 'padding': '10px 5px 10px 10px' }
            },
            bary: 'hover:bg-primary-400 bg-primary-300 opacity-100'
        }">
                <div class="card flex justify-content-center">
                    <Listbox v-model="selectedConversation" :options="Conversations" optionLabel="lastMessage"
                        class="w-full md:w-14rem" />
                </div>
            </ScrollPanel>
        </SplitterPanel>
        <SplitterPanel class="flex align-items-center justify-content-center space-around" :size="75">
            <ScrollPanel class="scroll-panel" style="width: 100%; height: 90%" :pt="{
            wrapper: {
                style: { 'border-right': '10px solid var(--surface-ground)', 'padding': '10px 5px 10px 10px' }
            },
            bary: 'hover:bg-primary-400 bg-primary-300 opacity-100'
        }">
                <div v-for="(conversation, id) in conversationHistory" :key="id">
                    <TextBox :name="conversation.name" :avatarImage="conversation.image" :message="conversation.text"
                        :type="conversation.type" />
                </div>
            </ScrollPanel>
            <div class="card flex justify-content-center p-inputgroup input-container">
                <Textarea v-model="dialog.text" placeholder="Message Chatbot..." autoResize rows="1" class="p-inputtext"
                    style="width: 100%;"></Textarea>
                <Button @click="sendMessage" icon="pi pi-send" aria-label="Send" style="min-width: auto;"></Button>
            </div>
        </SplitterPanel>
    </Splitter>
</template>

<style scoped lang="sass">
    @import "https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Roboto:wght@300;400;500;700&display=swap')
    template
        max-width: 100vw !important
        max-height: 100vh !important
    *
        font-family: 'Roboto', 'Poppins', sans-serif
    .p-listbox
        border: none        
    .scroll-panel 
        height: calc(100% - 20px)
        width: 100%
    .input-container 
        height: 10%
        width: 100%
        
    .newChatButton
        width: 100%
        height: 100%
        font-weight: 600
        font-size: 1.5rem
</style>