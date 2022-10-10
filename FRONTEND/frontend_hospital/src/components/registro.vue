<template>

    <section class="form-register">
        <h3> Formulario Regristro Usuario</h3>

        <form v-on:submit.prevent="processSignUp">
            <input class="controls" type="number"   v-model="user.id" name="id" id="id" placeholder="Ingrese Identificacion" >
            <input class="controls" type="text"     v-model="user.username" name="username" id="username" placeholder="Username" >
            <input class="controls" type="password" v-model="user.password" name="password" id="password" placeholder="Contraseña" >
            <input class="controls" type="text"     v-model="user.primerNombre" name="primerNombre" id="primerNombre" placeholder="Premier Nombre" >
            <input class="controls" type="text"     v-model="user.segundoNombre"  name="segundoNombre" id="segundoNombre" placeholder="Segundo Nombre" >
            <input class="controls" type="text"     v-model="user.primerApellido"  name="primerApellido" id="primerApellido" placeholder="Primer Apellido" >
            <input class="controls" type="text"     v-model="user.segundoApellido"  name="segundoApellido" id="segundoApellido" placeholder="Segundo Apellido" >
            <input class="controls" type="tex"      v-model="user.celular" name="celular" id="celular" placeholder="Celular" >
            <input class="controls" type="text"     v-model="user.pais" name="pais" id="pais" placeholder="Pais" >
            <input class="controls" type="text"     v-model="user.departamento" name="departamento" id="departamento" placeholder="Departamento" >
            <input class="controls" type="text"     v-model="user.municipio" name="municipio" id="municipio" placeholder="Municipio" >
            <input class="controls" type="text"     v-model="user.barrio" name="barrio" id="barrio" placeholder="Barrio" >
            <input class="controls" type="text"     v-model="user.direccion" name="direccion" id="direccion" placeholder="Direccion" >
            <input class="controls" type="email"    v-model="user.email" name="email" id="email" placeholder="Email / Correo Electronico" >
            <input class="controls" type="text"     v-model="user.account.especializacion" name="especializacion" id="especializacion" placeholder="Especializacion" >
            <input class="controls" type="text"     v-model="user.account.descripcion" name="descripcion" id="descripcion" placeholder="Descripciòn" >

            <button v-if="!is_auth"  v-on:click="logOut"  type="button" class="btn btn-danger">SALIR</button>

            <button type="submit"  class="btn btn-danger">GUARDAR</button>

            <button type="button" class="btn btn-dark">ROL</button>
        
        </form>

    </section>

</template>
  

<script>

    import axios from 'axios';

    export default{

        name:"signUp",
        data:function(){
            return{
                user:{
                    id: 0,
                    username: "",
                    password: "",
                    primerNombre: "",
                    segundoNombre: "",
                    primerApellido: "",
                    segundoApellido: "",
                    celular: "",
                    pais: "",
                    departamento: "",
                    municipio: "",
                    barrio: "",
                    direccion: "",
                    email: "",
                    account: [
                        {
                            especializacion: "si",
                            descripcion: "si",
                        }
                    ]
                }
            }
        },

        methods:{
            processSignUp: function() {
                axios.post(
                    "http://127.0.0.1:8000/usuario/",
                    this.user,
                    {headers:{}}
                )
                .then((result)=>{
                    let dataSignUp={
                        username: this.user.username,
                        token_access: result.data.access,
                        token_refresh: result.data.refresh
                    }

                    this.$emit('completedSignUp', dataSignUp)

                })

                .catch((error)=>{
                    console.log(error)
                    alert("error de registro del Usuario")

                });
                
            },

            loadSingUp:function(){
                this.$router.push({name:"signUp"})
            },
            
            veryfyAuth: function(){
                this.is_auth =  localStorage.getItem('isAuth') || false;
                if(this.is_auth == false){
                    this.$router.push({name:"logIn"})
                }else{
                    this.$router.push({name:"home"})
                }
            },
            
            
            logOut: function(){
                localStorage.clear();   
                 this.veryfyAuth();
                }
        }

    }

</script>
  
  

<style>
  
  *{
      margin: 0;
      padding: 0;
      box-sizing: border-box;
  }
  
  
  body{
      background-color:lightslategray;
  }
  
  
  .form-register{
      width: 500px;
      background: #24303c;
      padding: 20px;
      margin: auto;
      margin: 20px auto 20px auto;
      border-radius: 4px;
      font-family: 'calibri';
      color: white;
      box-shadow: 7px 13px 37px #000;
  }
  
  
  .form-register1{
      width: 500px;
      background: #24303c;
      padding: 20px;
      margin: auto;
      margin: 200px auto 20px auto;
      border-radius: 4px;
      font-family: 'calibri';
      color: white;
      box-shadow: 7px 13px 37px #000;
  }
  
  
  .form-register h3{
      font-size: 28px;
      margin-bottom: 20px;
      text-align: center;
      text-transform: uppercase
  }
  
  
  .controls{
      width: 100%;
      background:#f9fcfc;
      padding: 5px;
      border-radius: 10px;
      margin-bottom: 5px;
      border: 1px solid #1f53c5;
      font-family: 'calibri';
      font-size: 12px;
  
  }
  
  
  .form-register button{
      margin: 10px  10px  10px 20px;
      font-size: 14px;
  }
  
  
  .new-button{
      margin: 20px 10px 20px 120px;
      font-size: 14px;
      
  }
  
  
  .input-group{
      width: 100%;
      background:#f9fcfc;
      padding: 2px;
      border-radius: 10px;
      border: 1px solid #1f53c5;
      font-family: 'calibri';
      font-size: 12px;
  }
  
  footer{
  
      font-family: 'calibri';
      font-size: 10px;
      margin: 50px 10px;
      margin-bottom: 20px;
      text-align: center;
      text-transform: uppercase
  
  }
  
</style>
  