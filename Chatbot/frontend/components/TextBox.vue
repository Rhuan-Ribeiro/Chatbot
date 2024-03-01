<script setup>
    const props = defineProps({
        avatarImage: {type: String}, /* required: True faz o avatarImage ser obrigatório */
        name: {type: String},
        message: {type: String},
        type: {type: String},
    });



    // modo de comunicar props e css quando não h=a muitas variações
    // No Css é possivel acessar a variavel com v-bind(cardStyle.backColor)
    // const cardStyle = computed(()=> props.type === 'right' ? 
    // {
    //     backColor: '#90eebf',
    //     fontSize: '1.5rem',
    //     textColor: 'white'
    // } : {
    //     backColor: '#90ee90',
    //     fontSize: '1.5rem',
    //     textColor: 'white'
    // })
</script>

<template>
    <div class="text-box" :class="props.type === 'right' ? 'right-style' : 'left-style'">
        <Fieldset>
            <template #legend>
                <div class="flex align-items-center pl-2">
                    <Avatar :image="props.avatarImage" shape="circle" />
                    <span class="font-bold">{{ props.name }}</span>
                </div>
            </template>
            <p class="m-0">
                {{ props.message }}
            </p>
        </Fieldset>
    </div>
</template>

<style scoped lang="sass">
    .text-box 
        .p-fieldset
            font-size: 1rem
            color: #000
    .right-style
        .p-fieldset 
            background-color: var(--primary-300)
    .left-style  
        .p-fieldset 
            background-color: var(--primary-500)
    
</style>