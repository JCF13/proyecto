<template>
    <div id="main-camera" class="flex flex-center">
        <video class="align-middle">
            <source type="video/mp4">
        </video>
        <q-btn push label="HACER FOTO" color="black" />
    </div>
</template>

<script>
export default {
    data() {
        return {
            mediaRecorder: null
        }
    },
    created() {
        const constraints = { audio: true, video: { width: 1280, height: 720 } };
        let chunks = [];
        
        navigator.mediaDevices.getUserMedia(constraints).then((mediaStream) => {
            const video = document.querySelector("video");
            video.srcObject = mediaStream;

            this.mediaRecorder = new MediaRecorder(mediaStream);

            this.mediaRecorder.ondatavailable = function(e) {
                chunks.push(e.data)
            }

            video.play()
            this.mediaRecorder.start()
        })
    }
}
</script>

<style scoped>
    #main-camera {
        margin: 0 auto;
        width: 60%;
    }

    video {
        border: 5px solid black;
        border-radius: 10px;
        margin: 3%;
        height: 100%;
        width: 100%;
    }

    button {
        width: 25%;
        font-weight: bold;
    }
</style>