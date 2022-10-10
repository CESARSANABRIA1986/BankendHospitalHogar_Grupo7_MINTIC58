<template>
    <div>
     <section class="form-register">
        <h3> Formulario Login</h3>
        <form v-on:submit.prevent="processLogInUser">
            <input class="controls"  v-model="user.username" type="text" name="username" id="username" placeholder="Ingrese Identificacion" >
            <input class="controls" v-model="user.password"  type="password" name="password" id="password" placeholder="Username" >
  
            <div class="button">
                <button v-if="!is_auth" v-on:click="loadLogIn"   type="submit" class="btn btn-primary">LOGIN</button>
                <button v-if="!is_auth"  v-on:click="loadSingUp"   type="button" class="btn btn-primary">CREAR</button>
            </div>
        </form>
      </section>
    </div>
  </template>
  
  <script>
    import axios from 'axios';

    export default{

        name: "logIn",
        data:function(){
            return{
                user:{
                    username:"",
                    password:""
                }
            }
        },

        methods:{
            processLogInUser: function() {
                axios.post(
                    "http://127.0.0.1:8000/login/",
                    this.user,
                    {headers:{}}
                )
                .then(
                    (result)=>{
                        let dataLogin ={
                            username:this.user.username,
                            token_access: result.data.access,
                            token_refresh: result.data.refresh,
                        }

                        this.$emit('completedLogIn', dataLogin)
                    }
                    
                )

                .catch((error)=>{
                    if(error.response.status == "401" ){
                        alert("Error 401 :: usuario y Contraseña Incorrectas");
                    }

                }                
                
                )
            },

            loadSingUp:function(){
                this.$router.push({name:"signUp"})
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
  