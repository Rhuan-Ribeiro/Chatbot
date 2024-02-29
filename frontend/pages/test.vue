
<template>
    <div class="card flex justify-content-center">
        <Listbox v-model="selectedCity" :options="cities" optionLabel="name" class="w-full md:w-14rem" />
    </div>
</template>

<script setup>

const selectedCity = ref();
const cities = ref([
    { name: 'New York', code: 'NY' },
    { name: 'Rome', code: 'RM' },
    { name: 'London', code: 'LDN' },
    { name: 'Istanbul', code: 'IST' },
    { name: 'Paris', code: 'PRS' }
]);
</script>

<style scoped lang="sass">
    .p-listbox
        border: none
</style>