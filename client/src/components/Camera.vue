<template>
    <div>

    </div>
</template>

<script>
export default {
    name: 'Camera',
    data() {
        return {
            video: {},
            canvas: {},
            captures: []
        }
    },
    mounted() {
        this.video = this.$refs.video;
        if (navigator.mediaDevices && navigator.mediaDevices.getUserMedia) {
            navigator.mediaDevices.getUserMedia({video: true}).then(stream => {
                this.video.src = window.URL.createObjectURL(stream);
                this.video.play();
            })
        }
    },
    methods: {
        capture: function () {
            this.canvas = this.$refs.canvas;
            var context = this.canvas.getContext('2d').drawImage(this.video, 0, 0, 1920, 1080);
            this.captures.push(canvas.toDataURL('image/png'))
        }
    }
}
</script>