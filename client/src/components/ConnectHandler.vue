<template>
    <div class="mx-2">
        <v-icon>mdi-antenna</v-icon>
    </div>
</template>

<script>
export default {
    name: 'ConnectHandler',
    sockets: {
        connect: function () {
            console.log('connected')
        },
        test: function(data) {
            console.log(data)
        }
    }
}
</script>