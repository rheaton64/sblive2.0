<template>
    <div>
        <video ref='video' id='video'/>
    </div>
</template>

<script>
export default {
    name: 'Camera',
    data() {
        return {
            video: {}
        }
    },
    mounted() {
        this.video = this.$refs.video;
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({video: true}).then(stream => {
                //this.video.src = window.URL.createObjectURL(stream);
                this.video.srcObject = stream;
                this.video.play();
            })
        }
    },
    methods: {

    }
}
</script>