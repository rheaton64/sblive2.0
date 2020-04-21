<template>
    <v-card class='mx-auto' width='100%'>
        <v-container fluid>
            <v-row justify='center' align='center'>
                <v-col cols='auto'>
                    <v-btn large class='ma-5' v-on:click="baseClicked">Base Station</v-btn>
                    <v-btn large class='ma-5' v-on:click="controllerClicked">Controller</v-btn>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
export default {
    name: 'Start',
    methods: {
        baseClicked: function () {
            this.$socket.emit('create_instance')
            this.$emit('init-base')
            console.log('am base')
        },
        controllerClicked: function () {
            this.$emit('init-controller')
            console.log('am controller')
        }
    }
}
</script>