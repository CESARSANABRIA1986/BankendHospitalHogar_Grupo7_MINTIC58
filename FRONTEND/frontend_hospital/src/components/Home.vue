<template>

<section class="form-register">
        <h3> Formulario Login</h3>
        <form>
            <span>
                <h1>Bienvenido Usuario(a) {{username}}</h1>
            </span>
        </form>
        <div class="button">
                <button v-if="!is_auth"   v-on:click="logOut" type="button" class="btn btn-danger">SALIR</button>
        </div>
      </section>

    <div>

    </div>

</template>


<script>
    export default{
        name:"home",
        data:function(){
            return{
            username:localStorage.getItem('username') || 'none'
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

    logOut: function(){
        localStorage.clear();
        alert("Seccion cerrada con Exito !");
        this.veryfyAuth();

},   

created: function(){
    this.veryfyAuth()

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

