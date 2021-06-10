<template>
    <div id="main-camera" class="flex flex-center">
        <video class="align-middle">
            <source type="video/mp4">
        </video>
        <q-btn push label="HACER FOTO" color="black" @click="nextDialog" />
        <input type="hidden" id="picture">
        <q-dialog v-model="captionDialog">
            <q-card style="width: 700px; max-width: 80vw;">
                <img id="photo" src="" alt="">
                <q-card-section>
                    <div class="text-h6">Añade un pie de foto si lo ves necesario</div>
                </q-card-section>

                <q-card-section class="q-pt-none">
                    <q-input color="black" v-model="caption" autofocus='true'/>
                </q-card-section>

                <q-card-actions align="right" class="bg-white">
                    <q-btn flat label="CANCELAR" @click="captionDialog = false"/>
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
            picture: ''
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
                    document.querySelector('#picture').value = btoa(e.target.result);
                }

                reader.readAsBinaryString(blob);
                document.querySelector('#photo').src = url;
            })


            this.captionDialog = true;
        },
        async createPost() {
            const postFetch = await this.$axios.post('https://localhost:5000/post/cpost',
            {
                caption: this.caption,
                picture: document.querySelector('#picture').value
            },
            {
                headers: {
                    'Authorization': 'Bearer ' + localStorage.getItem('access_token'),
                    'Content-type': 'application/json'
                }
            });

            const response = postFetch.data;

            if (!response.error_type) {
                this.$q.notify({
                    type: 'positive',
                    message: 'Publicación creada correctamente',
                    position: 'top-right'
                })
                this.$router.push(`/inside/home/post/${response.response.post_id}`)
            } else this.$q.notify({
                type: 'error',
                message: response.error_desc,
                position: 'top-right'
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