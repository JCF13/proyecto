<template>
    <div id="main-newpost">
        <q-form>
            <div>
                <img src="https://www.hola.com/imagenes/viajes/20180530124901/naturaleza-destinos-mundo-a-todo-color/0-571-947/colores-m.jpg" alt="">
            </div>
            
            <q-input
                filled
                label="Pie de foto"
                color="black"
            >
                <template v-slot:prepend>
                    <q-icon color="black" name="format_quote"/>
                </template>
            </q-input>

            <q-btn label="GUARDAR" type="button" color="black" id="guardar"/>
        </q-form>
    </div>
</template>

<script>
export default {
    
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Nunito:wght@200;700&display=swap');
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }

    #main-newpost {
        padding: 5%;
        width: 60%;
        margin: 0 auto;
    }

    img {
        width: 50%;
        border-radius: 10px;
    }

    form {
        display: grid;
    }

    #guardar {
        margin-top: 1%;
        justify-self: right;
        width: 25%;
        border-radius: 10px;
        font-weight: bold;
    }
</style>