<template>
    <div id="main-camera" class="flex flex-center">
        <video class="align-middle">
            <source type="video/mp4">
        </video>
        <q-btn push label="HACER FOTO" color="black" @click="nextDialog" />

        <q-dialog v-model="captionDialog">
            <q-card style="width: 700px; max-width: 80vw;">
                <img id="photo" src="" alt="">
                <q-card-section>
                    <div class="text-h6">Añade un pie de foto si lo ves necesario</div>
                </q-card-section>

                <q-card-section class="q-pt-none">
                    <q-input color="black" v-model="caption"/>
                </q-card-section>

                <q-card-actions align="right" class="bg-white">
                    <q-btn flat label="SIGUIENTE" @click="createPost" />
                </q-card-actions>
            </q-card>
        </q-dialog>
    </div>
</template>

<script>
export default {
    data() {
        return {
            mediaRecorder: null,
            captionDialog: false,
            caption: '',
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
    },
    methods: {
        nextDialog() {
            let canvas = document.createElement('CANVAS');
            let video = document.querySelector('video');
            canvas.width = video.videoWidth;
            canvas.height = video.videoHeight;

            let ctx = canvas.getContext('2d');
            ctx.drawImage(video, 0, 0);

            ctx.canvas.toBlob(async function(blob) {
                let url = URL.createObjectURL(blob);
                var reader = new FileReader();
                reader.onload = function(e) {
                    let fileInBase64 = btoa(e.target.result);
                }

                reader.readAsBinaryString(blob);
                document.querySelector('#photo').src = url;
            })

            this.captionDialog = true;
        },
        async createPost() {
            const authorization = localStorage.getItem('access_token');
            const postFetch = await fetch('http://localhost:5000/post/cpost', {
                method: 'POST',
                headers: {
                    'Authorization': JSON.stringify(authorization)
                },
                body: JSON.stringify({
                    caption: this.caption,
                    path: 'C:\\Users\\JCFJe\\Documentos\\Segundo_curso\\FCP\\proyecto\\backend\\flask_app\\app\\static\\img',
                    fname: 'primerafoto'
                })
            })
        }
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

    #photo {
        width: 100%;
        height: 100%;
        margin: 0 auto;
    }
</style>