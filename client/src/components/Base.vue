<template>
<div width='100%' class='ma-auto'>
    <v-card class='my-2' width='100%'>
        <v-container fluid>
            <v-row justify="space-between" align="center">
                <v-col cols="auto">
                    <v-card-title>Base Station Code: {{ code }}</v-card-title>
                </v-col>
                <v-col cols='auto'>
                    <v-alert dense :value="alert_new" type="success" transition="scale-transition" width="100%">New Point!</v-alert>
                    <v-alert dense :value="alert_replay" type="warning" transition="scale-transition" width="100%">Replay!</v-alert>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
    <v-card class="pa-4 my-2">
        <Camera />
    </v-card>
</div>
</template>

<script>
import Camera from '@/components/Camera'

export default {
    name: 'Base',
    components: {
        Camera
    },
    data() {
        return {
            message: 'Nothing',
            code: '',
            alert_new: false,
            alert_replay: false
        }
    },
    sockets: {
        get_code: function(data) {
            this.code = data
        },
        action: function(data) {
            if(data == 'new_point') {
                this.alert_new = true;
                setTimeout(() => {
                    this.alert_new = false
                }, 2000)
            }
            if(data == 'replay') {
                this.alert_replay = true;
                setTimeout(() => {
                    this.alert_replay = false
                }, 2000)
            }
        },
        new_controller: function () {
            console.log('New controller connected')
        }
    }
}
</script>