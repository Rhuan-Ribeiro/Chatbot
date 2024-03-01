<script setup lang="ts">

</script>

<template>
    <main class="login_main">
        <section class="logo_panel">
            <img src="/sge.jpeg" alt="sge logo">
            <h1>Sistema de Gestão de Ensino</h1>
            <div class="stars1"></div>
            <div class="stars2"></div>
            <div class="stars3"></div>
        </section>
        <section class="login_panel">
            <h1>Sou o Login!</h1>
        </section>
    </main>
</template>

<style scoped lang="sass">
    .login_main
        width: 100vw 
        height: 100vh
        display: flex
        background-color: var(--light-background-color)
    .logo_panel
        display: none
    .login_panel
        width: 100vw
        height: 100vh
    img
        width: 250px
        height: 250px
    @media screen and (min-width: 600px)
        .logo_panel, .login_panel
            width: 50vw
            height: 100vh
        .logo_panel
            display: flex
            flex-direction: column
            align-items: center
            justify-content: center
            background-color: var(--dark-background-color)
</style>