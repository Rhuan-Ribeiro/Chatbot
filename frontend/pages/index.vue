<script setup>
        const testHistory = async () => {
            let historyId = 39;
            const {data: getHistory} = await useFetch('http://localhost:8000/chatbot/',{
                // method: 'GET',
                body:{
                    // userId: 2,
                    "conversationId": historyId
                }   
            })
            //console.log("type:", getHistory.value.type)
            console.log("message:", getHistory)
            // console.log("id:", getHistory.value.id)
            // console.log("fetch:", getHistory)
        }
        
    
    

    let response = ref("")
    const dialog = reactive({
        text: '',
        type: '',
        name: '',
        image: '',
        historyId: null
    });

    const includeDialog = ((type)=>{
        if(type === 'Q'){
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
        console.log(conversationHistory.value);
    });
    
    const sendMessage = async () => {
        console.log(dialog.text);
        includeDialog('Q');
        
        //message.value;
        const {data: answer} = await useFetch('http://localhost:8000/chatbot/',{
            method: 'POST',
            body:{
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
    <div>
        <div v-for="(conversation, id) in conversationHistory" :key="id">
            <TextBox :name="conversation.name" :avatarImage="conversation.image" 
                :message="conversation.text" :type="conversation.type"/>
        </div>

        <!-- <div v-for="(conversation, id) in getHistory" :key="id">
            <p> {{ conversation.value.message  }}</p>        
        </div> -->
        <div class="card flex justify-content-center align-items-center">
            <Textarea v-model="dialog.text" placeholder="Message Chatbot..." autoResize rows="1" cols="25" />
            <Button @click="sendMessage" icon="pi pi-send" aria-label="Filter"></Button>
            <Button @click="testHistory" icon="pi pi-server" aria-label="Filter"></Button>
        </div>
        
        <hr>
        <div>
            <h5>Bard: 😎</h5>
            <p> {{  }} </p>
        </div>
    </div>
</template>

<style scoped>
</style>