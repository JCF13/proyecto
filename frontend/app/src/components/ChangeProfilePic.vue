<template>
    <div id="change-profilepic-main">
        <h4>Cambiar foto de perfil</h4>
        <input type="hidden" id="picture-new">
        <q-form id="form-profilepic">
            <video id="profile-new" class="align-middle">
                <source type="video/mp4">
            </video>

            <div id="new-pic">
                Foto
            </div>

            <q-btn label="GUARDAR" type="button" color="black" style="height: 100%;" @click="changePicture"/>
        </q-form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            model: null
        }
    },
    created() {
        const constraints = { audio: false, video: { width: 1280, height: 720 } };
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
    },
    methods: {
        async changePicture() {
            let canvas = document.createElement('CANVAS');
            let video = document.querySelector('#profile-new');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;

            let ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0);
            ctx.canvas.toBlob(async (blob) => {
                let url = URL.createObjectURL(blob);
                var reader = new FileReader();
                reader.onload = async (e) => {
                    document.querySelector('#picture-new').value = btoa(e.target.result);
                    const profileFetch = await fetch('https://localhost:5000/my/profilepic', {
                        method: 'POST',
                        headers: {
                            'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                            'Content-type': 'application/json'
                        },
                        body: JSON.stringify({
                            'picture': btoa(e.target.result)
                        })
                    });
                    const resp = await profileFetch.json();

                    if (resp.type === 'positive') {
                        this.$q.notify({
                            type: 'positive',
                            message: resp.message,
                            position: 'top-right'
                        })
                    }
                }

                reader.readAsBinaryString(blob);
            })
        },
    }
}
</script>

<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    #change-profilepic-main {
        padding-top: 5%;
        height: 100%;
        width: 100%;
    }

    #form-profilepic {
        height: 70%;
        width: 90%;
        display: grid;
    }

    #form-profilepic button {
        width: 25%;
        height: 50%;
        justify-self: right;
    }

    #new-pic {
        height: 100%;
    }

    video {
        border-radius: 10px;
        height: 100%;
        width: 100%;
    }
</style>