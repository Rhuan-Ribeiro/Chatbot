<script setup>
const dialog = reactive({
    text: '',
    type: '',
    name: '',
    image: '',
    historyId: null
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
        dialog.historyId = null;
    }
}

Messages(39);

const sendMessage = async () => {
    console.log(dialog.text);
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
    dialog.text = answer.value.message
    dialog.historyId = answer.value.history.id
    includeDialog('A');
    dialog.text = '';
}

//armazena em tela o histórico das mensagens
const conversationHistory = ref([])
</script>

<template>
    <Splitter style="height: 98vh">
        <SplitterPanel class="flex align-items-center justify-content-center" :size="25" :minSize="10">
            <ScrollPanel>
                Panel 1
            </ScrollPanel>
        </SplitterPanel>
        <SplitterPanel class="flex align-items-center justify-content-center" :size="75">
            <ScrollPanel style="width: 100%; height: 94%" :pt="{
                wrapper: {
                    style: { 'border-right': '10px solid var(--surface-ground)', 'margin-bottom': '5px' }
                },
                bary: 'hover:bg-primary-400 bg-primary-300 opacity-100'
            }">
                <div v-for="(conversation, id) in conversationHistory" :key="id">
                    <TextBox :name="conversation.name" :avatarImage="conversation.image" :message="conversation.text"
                        :type="conversation.type" />
                </div>
            </ScrollPanel>
            <div class="card flex justify-content-center p-inputgroup" style="width: 100%;">
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
        max-width: 100vw
        max-height: 100vh
    *
        font-family: 'Roboto', 'Poppins', sans-serif
</style>