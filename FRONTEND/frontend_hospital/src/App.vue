<template>

<div>
  <div>
    <router-view v-on:completedLogIn="completedLogIn" v-on:completedSignUp="completedSignUp">
    </router-view>
  </div>

  <footer>
    <span>
      <p>Derechos Reservados MINTIC2022 </p>
    </span>
    <span><p>TIC 2022 Universidad Nacional Colombia</p></span>
    <span><p> By. Ing. Cesar Augusto Sanabria</p></span>
  </footer>

</div>

</template>


<script>
  import{tsImportEqualsDeclaration} from '@babel/types'

  export default{
    name:'App',

    data: function(){
      return{
        is_auth:false

      }

    },

    methods:{
      veryfyAuth: function(){
        this.is_auth =  localStorage.getItem('isAuth') || false;
        if(this.is_auth == false){

          this.$router.push({name:"logIn"})

        }else{

          this.$router.push({name:"home"})

        }

      },

      loadLogIn: function(){

        this.$router.push({name:"logIn"})
        
      },

      completedLogIn:function(data){
        
        localStorage.setItem("isAuth", true);
        localStorage.setItem("username", data.username);
        localStorage.setItem("token_access", data.token_access);
        localStorage.setItem("token_refresh", data.token_refresh);

        alert("ingresaste Correctamente a la Aplicación");
        this.veryfyAuth();

      },


      completedSignUp: function(data){

        alert( "Usuario Registrado Exitoso !!" )
        //this.completedLogIn(data)

      },

      
      logOut: function(){

        localStorage.clear();
        alert("Seccion cerrada con Exito !");
        this.veryfyAuth();

      }, 


      loadSingUp:function(){
        this.$router.push({name:"signUp'"})
      }

    },


    created: function(){

      this.veryfyAuth()

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
