<template>
    <v-card class='mx-auto' width='100%'>
        <v-container>
            <v-row justify='center' align='center'>
                <v-col cols='auto' class='text-center'>
                   <form @submit="connectToCode">
                       <input type="text" v-model="code" name="code" placeholder="Base Station Code...">
                       <input type="submit" value="Submit" class='btn'>
                   </form>
                </v-col>
            </v-row>
        </v-container>
    </v-card>
</template>

<script>
export default {
    name: 'CodeInput',
    data() {
        return {
            code: ''
        }
    },
    methods: {
        connectToCode: function(e) {
            e.preventDefault()
            this.$emit('connect-to', this.code)
            this.code = ''
        }
    }
}
</script>

<style scoped>
    .btn {
        background-color: #333333;
        border-radius: 5px;
        padding: 7px 20px;
        color: white;
    }
    .btn:hover {
        background-color: #474747;
    }

</style>