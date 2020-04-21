<template>
   <div>
       <CodeInput class='ma-4' v-on:connect-to="connectToBase"/>
       <v-card class='my-2' width='100%' v-if="connected">
           <v-card-title>Base Station Code: {{ code }}</v-card-title>
       </v-card>
        <v-card class='mx-auto' width='100%' v-if="connected">
            <v-container>
                <v-row justify='center' align='center'>
                    <v-col cols='auto' class='text-center'>
                    <v-btn large class="ma-5" color='primary' v-on:click="controllerAction('new_point')">New Point</v-btn>
                    <v-btn large class="ma-5" color='error' v-on:click="controllerAction('replay')">Replay</v-btn>
                    </v-col>
                </v-row>
            </v-container>
        </v-card>
    </div>
</template>

<script>
import CodeInput from '@/components/CodeInput'

export default {
    name: 'Controller',
    components: {
        CodeInput
    },
    data() {
        return {
            code: '',
            index: -1,
            connected: false
        }
    },
    sockets: {
        get_index: function(data) {
            this.index = data
            this.connected = true
            console.log('Index of controller is '+this.index)
        }
    },
    methods: {
        connectToBase: function (code) {
            this.code = code
            this.$socket.emit('add_controller', this.code)
        },
        controllerAction: function (act) {
            const data = {
                act: act,
                index: this.index
            }
            this.$socket.emit('action', data)
        }
    }
}
</script>