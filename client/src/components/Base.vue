<template>
<div>
    <v-card class='my-2' width='100%'>
        <v-card-title>Base Station Code: {{ code }}</v-card-title>
    </v-card>
    <v-card class='mx-auto' width='100%'>
        <v-container>
            <v-row justify='center' align='center'>
                <v-col cols='auto' class='text-center'>
                   <h1>You are a Base Station</h1>
                   <h2>The most recent ping was: {{ message }}</h2>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</div>
</template>

<script>
export default {
    name: 'Base',
    data() {
        return {
            message: 'Nothing',
            code: ''
        }
    },
    sockets: {
        get_code: function(data) {
            this.code = data
        },
        action: function(data) {
            this.message = data
        },
        new_controller: function () {
            console.log('New controller connected')
        }
    }
}
</script>