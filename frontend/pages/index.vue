<script setup>
    
    const dialog = reactive({
        message: '',
        type: '',
        name: '',
        image: ''
    });

    const includeDialog = ((type)=> {
        if(type === 'Question') {
            dialog.image = 'user.png'
            dialog.name = 'Rhuan'
            dialog.type = 'right'
        } else {
            dialog.image = 'bot.png'
            dialog.name = 'Bot'
            dialog.type = 'left'
        }

        // realizando a DEEP COPY da estrutura apenas com os valores atuais.
        conversationHistory.value.push(
            JSON.parse(JSON.stringify(dialog))
        );
    }) 

    const sendMessage = async () => {
        console.log(dialog);
        includeDialog('Question')
        
        //message.value;
        const {data: answer} = await useFetch('http://localhost:8000/chatbot/',{
            method: 'POST',
            body:{
                question: dialog.message
            }
        })
        dialog.message = answer.value.content
        includeDialog('Answear')
    }

    // armazena em tela o histórico das mensagens
    const conversationHistory = ref([]);
</script>

<template>
    <div>
        <div v-for="(conversation, id) in conversationHistory" :key="id">
            <TextBox :name="conversation.name" :avatarImage="conversation.image" :message="conversation.message" :type="conversation.type"/>
        </div>
    
        <!-- <TextBox name="Bot" avatarImage="bot.png" message="Lorem ipsum dolor sit amet consectetur adipisicing elit. Commodi, sint illo. Ex, at. Eum, commodi." type="left"/> -->
        <label for=""> Type here your message!</label> <br>
        <textarea v-model="dialog.message"/> <br> <br>
        <Button @click="sendMessage" label="Send"></Button>
        <hr>
        <div>
            <h5>Bard: 😊</h5>
            <p>{{ response }}</p>
            <i class="pi pi-check"></i>
        </div>
    </div>
</template>

<style scoped>
  
    /* button{
        background-color: black;
        color: white;
    } */
</style>