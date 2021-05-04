<template>
    <q-dialog v-model="alert" persistent>
        <q-card id="my-card">
            <q-card-section horizontal>
                <div id="card-left">
                    <q-icon id="close" name="highlight_off" size="30px" @click="close"/>

                    <img id="image" src="https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg" alt="">
                
                    <div id="pie-de-foto" class="absolute-bottom text-subtitle2">
                        Pie de foto 
                    </div>
                </div>

                <q-card-actions vertical id="card-right">
                    <div id="modal-user">
                        <q-avatar size="30px" class="avatar" color="orange">J</q-avatar>
                        <h6>Usuario</h6>
                    </div>
                    <div id="modal-info">
                        <div>
                            <p>34</p><q-icon size="15px" name="favorite" color="red" /> 
                            <q-icon name="favorite" style="display:none;" />
                        </div>
                        <div>
                            <p>4</p>
                            <q-icon name="comment" />
                        </div>
                    </div>
                    <div id="creation-date">
                        <p>14-3-2021</p>
                    </div>
                    <div id="comments">
                        <div>
                            <q-avatar size="20px" class="avatar" color="blue">J</q-avatar>
                            <p><span>Usuario1.</span> Comentario 1</p>
                        </div>
                        <div>
                            <q-avatar size="20px" class="avatar" color="orange">J</q-avatar>
                            <p><span>Usuario2.</span> Comentario 2</p>
                        </div>
                        <div>
                            <q-avatar size="20px" class="avatar" color="red">J</q-avatar>
                            <p><span>Usuario3.</span> Comentario 3</p>
                        </div>
                        <div>
                            <q-avatar size="20px" class="avatar" color="green">J</q-avatar>
                            <p><span>Usuario4.</span> Comentario 4</p>
                        </div>
                        <div>
                            <q-avatar size="20px" class="avatar" color="pink">J</q-avatar>
                            <p><span>Usuario5.</span> Comentario 5</p>
                        </div>
                        <div>
                            <q-avatar size="20px" class="avatar" color="purple">J</q-avatar>
                            <p><span>Usuario6.</span> Comentario 6</p>
                        </div>
                        <div>
                            <q-avatar size="20px" class="avatar" color="yellow">J</q-avatar>
                            <p><span>Usuario7.</span> Comentario 7</p>
                        </div>
                        <div>
                            <q-avatar size="20px" class="avatar" color="orange">J</q-avatar>
                            <p><span>Usuario8.</span> Comentario 8</p>
                        </div>
                        <q-icon name="add_circle_outline" size="25px"/>
                    </div>
                    <div id="new-comment">
                        <q-input label="Escribe un comentario" color="black">
                            <template v-slot:append>
                                <q-icon name="send" color="black"/>
                            </template>
                        </q-input>
                    </div>
                </q-card-actions>
            </q-card-section>
        </q-card>
    </q-dialog>
</template>

<script>
export default {
    data() {
        return {
            alert: true
        }
    },
    methods: {
        close() {
            this.$router.go(-1)
        }
    }
}
</script>

<style scoped>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #my-card {
        width: 100%;
        max-width: 800px;
    }

    #image {
        justify-self: center;
        max-width: 400px;
        max-height: 500px;
        align-self: center;
    }

    #card-left {
        display: grid;
        width: 50%;
        height: 500px;
        border-right: 2px solid grey;
        margin: 0 auto;
    }

    #card-right {
        padding: 1%;
        width: 50%;
        display: grid;
        grid-template-columns: 50% 50%;
        grid-template-rows: 10% 10% 70% 10%;
        grid-template-areas: 
            "user info"
            "fecha fecha"
            "comments comments"
            "comment comment";
    }

    #modal-user {
        grid-area: user;
        display: grid;
        grid-template-columns: 20% 80%;
    }

    #modal-info {
        padding-right: 5%;
        grid-area: info;
        display: grid;
        grid-template-rows: 50% 50%;
        justify-items: right;
    }

    #modal-info div:first-child {
        display: grid;
        grid-template-columns: 90% 10%;
    }

    #modal-info div:last-child {
        display: grid;
        grid-template-columns: 90% 10%;
    }

    #creation-date {
        grid-area: fecha;
    }

    span {
        font-weight: bold;
    }

    #close {
        position: absolute;
        margin: 1%;
    }

    #close {
        cursor: pointer;
    }

    #comments {
        grid-area: comments;
        display: grid;
    }

    #comments div {
        display: grid;
        grid-template-columns: 10% 90%;
        margin-bottom: 5%;
    }

    #comments i:last-child {
        justify-self: center;
    }

    #pie-de-foto {
        background: rgba(0, 0, 0, 0.692);
        width: 50%;
        color: white;
        text-align: left;
        padding: 1%;
        height: 7%;
    }

    #new-comment {
        grid-area: comment;
    }

</style>