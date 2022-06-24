<template>
  <section id="login">
    
    <div class="landing-container">
      <h1>Welcome to IFTTT</h1>
      <p><a @click="subscribe = false">Sign in</a> or <a @click="subscribe = true">Sign up</a></p>
      <p>to continue access</p>
      <i class="obj0"></i>
      <i class="obj1"></i>
      <img :src="require('@/assets/screenifttt.png')" :alt="'logo ifttt'" />
    </div>

    <transition name="fade">
    <div v-show="!subscribe" class="login-container">
      <div class="form-container">
        <h2>Sign in</h2>
        <div class="input">
          <input type="text" v-model="username" required>
          <label>Username</label>
        </div>
        <div class="input">
          <input @keyup.enter="login()" type="password" v-model="password" required>
          <label>Password</label>
        </div>
        <p class="error">{{error}}</p>
        <a @click="login()" class="btn-0"><span>Sign in</span></a>
        <div class="container-p"><p>Or sign in using Google</p></div>
        <a v-google-signin-button="clientId" class="btn-1"><span><img :src="require('@/assets/google.png')" :alt="'google'"/><p>Sign in With Google</p></span></a>
      </div>
    </div>
    </transition>

    <transition name="fade">
    <div v-show="subscribe" class="login-container">
      <div class="form-container">
        <h2>Sign up</h2>
        <div class="input">
          <input type="text" v-model="username" required>
          <label>Username</label>
        </div>
        <div class="input">
          <input type="text" v-model="email" required>
          <label>Email Address</label>
        </div>
        <div class="input">
          <input type="password" v-model="password" required>
          <label>Password</label>
        </div>
        <div class="input">
          <input @keyup.enter="register()" type="password" v-model="password2" required>
          <label>Retype Password</label>
        </div>
        <p class="error">{{error}}</p>
        <a @click="register()" class="btn-0"><span>Sign up</span></a>
        <div class="container-p"><p>Or sign up using Google</p></div>
        <a v-google-signin-button="clientId" class="btn-1"><span><img :src="require('@/assets/google.png')" :alt="'google'"/><p>Sign up With Google</p></span></a>
      </div>
    </div>
    </transition>

  </section>
</template>

<script>
import axiosGet from '@/assets/script/api.js' 

export default {
  name: 'Login',
  props: {
  },
  data () {
    return {
      subscribe: false,
      username: '',
      email: '',
      password: '',
      password2: '',
      error: '',
      clientId: '250030754484-21ifq36jidj4kofjmgu08vlm3ihkukb3.apps.googleusercontent.com'
    }
  },
  methods: {
    async login() {
      if (this.username == '' || this.password == '') {
        this.error = 'Error: you need to enter email and password'
        return 84
      } else {
        let payload = {'username': this.username, 'password': this.password}
        await axiosGet.post('/login/', payload)
        .then((response) => {
          if (!response.data.error) {
            this.error = ''
            this.email = ''
            this.password = ''
            localStorage.setItem('token', response.data.token)
            this.$router.push('/')
          } else {
            this.password = ''
            this.error = 'Error on username or login'
          }
        }).catch((error) => {
          console.log(error)
          this.error = 'Error on username or login'
          this.email = ''
          this.password = ''
        })
      }
      return 0
    },
    async register() {
      if (this.username == '' || this.email == '' || this.password == '' || this.password2 == '') {
          this.error = 'Error: you need to enter username, email and password'
          return 84
      } else if (this.password != this.password2) {
        this.error = 'Error: the second password need to be the same as the first'
        this.password2 = ''
        this.password2 = ''
        return 84
      } else {
        let payload = {'username': this.username, 'email': this.email, 'password': this.password}
        await axiosGet.post('/register/', payload)
        .then(() => {
          this.subscribe = true
          this.password = ''
          this.password2 = ''
          this.username = ''
          this.email = ''
        })
        .catch(() => {
          this.error = "User already exist"
        })
      }
      return 0
    },
    async googleRequest (idToken) {
      console.log(idToken)
      let payload = {'googleToken': idToken}
      await axiosGet.post('/googleregister/', payload)
      .then(response => {
        console.log(response)
        this.error = ''
        this.email = ''
        this.password = ''
        localStorage.setItem('token', response.data.token)
        this.$router.push('/')
      })
      .catch(error => {
        console.log(error)
      })
    },
    OnGoogleAuthSuccess (idToken) {
      this.googleRequest(idToken)
    },
    OnGoogleAuthFail (error) {
      console.log(error)
    }
  },
  mounted () {
    
  }
}
</script>

<style scoped lang="scss">
$primary-color: #362490;
$secondary-color: #5721AB;
$third-color: #551778;
$four-color: #B211AD;
$rose: #ff35ae;
$red: #c60d48;
$blue: #2aadd9;

#login {
  display: flex;
  max-width: 100vw;
  height: 100vh;
  max-height: 100vh;

  .landing-container {
    display: flex;
    align-items: center;
    flex-direction: column;
    min-width: 50vw;
    height: 100%;
    background-image: linear-gradient(130deg, $primary-color, $four-color);

    h1 {
      margin-top: 30vh;
      font-size: 3em;
      color: white;
      z-index: 2;
    }

    p {
      color: white;
      z-index: 2;

      a {
        transition: text-decoration 500ms;
        &:hover {
          color: lightgrey;
          text-decoration: underline;
          cursor: pointer;
        }
      }

    }

    img {
      position: absolute;
      top: 1vh;
      left: 2vw;
    }

    i {
      position: absolute;
      z-index: 1;
      border-radius: 50%;
    }

    .obj0 {
      width: 100px;
      height: 100px;
      top: 23vh;
      left: 11vw;
      background-image: linear-gradient(130deg, $secondary-color, $third-color);
    }

    .obj1 {      
      width: 200px;
      height: 200px;
      top: 30vh;
      left: 30vw;
      background-image: linear-gradient(130deg, $primary-color, $four-color);
    }
  }

  .login-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    max-width: 44vw;
    height: 60vh;
    padding: 20vh 3vw;
    min-width: 400px;

    h2 {
      font-size: 2em;
    }

    .form-container {
      width: 44vw;
      height: 100%;
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      .error {color: $four-color;}

      .input {
        position: relative;
        width: 100%;

        label {
          left: 0px;
          position: absolute;
          transition-duration: 600ms;
          color: lightgrey;
          pointer-events: none;
        }

        input {
          padding: 10px 0;
          width: 100%;
          box-sizing: border-box;
          box-shadow: none;
          outline: none;
          border: none;
          border-bottom: 2px solid $primary-color;

          &:focus ~ label, &:valid ~ label {
            top: -20px;
            left: 0px;
            color: $four-color;
            font-size: 12px;
            font-weight: bold;
          }

          &:focus, &:active, &:valid {
            border-bottom: 2px solid $four-color;
          }
        }
      }
    }

    .container-p {
      color: lightgrey;
      display: flex;
      justify-content: center;
      width: 100%;
    }
  }
      
}

@media (max-width: 900px) {

  #login {
    display: flex;
    flex-direction: column;

    .login-container {
      padding: 10vh 10vw;
      min-width: 80vw;
      .form-container {
        width: 80vw;
      }
    }
    .landing-container {
      min-width: 100vw;
    }
  }
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}

</style>