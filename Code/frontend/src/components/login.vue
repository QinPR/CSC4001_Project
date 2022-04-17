<template>
  <div id="body">
    <div class="container-login">
      <div class="header-login">
        <div class="header-login-box">
          <span class="header-text-position">
            <router-link to="/register"
               id="register">&nbsp;<i class="fa fa-user-plus"></i>&nbsp;&nbsp;Sign Up</router-link>
          </span>
          <router-link to="/forgot"
             id="forgetpassword"><i class="fa fa-question"></i>&nbsp;&nbsp;Forgot Password?</router-link>
        </div>
      </div>
      <div class="logo">
          <div class="switch-left">
            <div class="pad-left"></div>
          </div>
          <div class="switch-right">
            <div class="pad-right"></div>
          </div>
          <div class="text">
          <p class="nintendo-text">cuhksz</p>
          <p class="switch-text">OverFlow</p>
          </div>
      <svg class="clack-svg">
        <line x1="25" y1="90" x2="50" y2="15" stroke-linecap="round"/>
        <line x1="47" y1="107" x2="120" y2="30" stroke-linecap="round"/>
        <line x1="65" y1="130" x2="137" y2="100" stroke-linecap="round"/>
      </svg>
    </div>
      <div class="login-box">
        <div class="login">
          <h1>Authentication</h1>
          <input id="username"
                 type="text"
                 placeholder="username"
                 @keyup.enter="submit"
                 v-model="username" />
          <label for="username"
                 class="login-input-icon">
            <i class="fa fa-user"></i>
          </label>
          <input id="password" v-if="showPassword" type="text" class="input" v-model="password" @keyup.enter="submit" />
          <input id="password" v-else type="password" class="input" v-model="password" placeholder="Password" @keyup.enter="submit" >
          <label for="password"
                 class="login-input-icon">
            <i v-if="showPassword" class="fa fa-eye" @click="toggleShow"></i>
            <i v-if="!showPassword" class="fa fa-eye-slash" @click="toggleShow"></i>
          </label>
          <div class="login-remember">
            <label class="login-checkbox">
              <input type="checkbox">
              <span class="checkmark"></span>
            </label>
            <span class="login-remember-text">
              &nbsp;&nbsp;Remember
            </span>
          </div>
          <button  @click="submit" >Login</button>
          <span class="login-separator"></span>
          <div class="login-social-media">
             <div class="circle"><div class="wave"> </div> </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Qs from 'qs'
export default{
  name: 'login',
  data () {
    return {
      showPassword: false,
      showDiv: true,
      username: '',
      password: ''
    }
  },
  computed: {
    buttonLabel () {
      return (this.showPassword) ? 'Hide' : 'Show'
    }
  },
  methods: {
    toggleShow () {
      this.showPassword = !this.showPassword
    },
    submit () {
      if (this.username === '' || this.password === '') {
        this.$message.error('please input your username and password!')
      } else {
        let sendData = {
          username: this.username,
          password: this.password
        }
        axios({
          method: 'POST',
          url: 'http://175.178.34.84/login/',
          data: Qs.stringify(sendData)
        }).then((response) => {
          if (response.data === 'Success Login!') {
            this.$message.success('Welcome!')
            this.$router.push({
              path: '/home/:username',
              name: 'home',
              params: {
                username: this.username
              }
            })
          } else {
            this.$message.error(response.data)
          }
        })
      }
    }
  }
}
</script>

<style scoped>
@import url("../font-awesome-4.7.0/css/font-awesome.min.css");

* {
  padding: 0;
  margin: 0;
  border: 0;
  outline: 0;
}

html {
  line-height: 1.15;
  -webkit-text-size-adjust: 100%;
  margin: 0;
  padding: 0;
}
#body {
  background: linear-gradient(-218deg, #206475 48%, #2f9aa8 75%);
  font-family: 'Poppins', sans-serif;
  height: 100vh;
}
.logo {
  transform: scale(0.24);
  position: absolute;
  top: 4vh;
  left: 38%;
}

.switch-left {
  position: fixed;
  background: transparent;
  width: 130px;
  height: 380px;
  border-radius: 50px 5px 25px 150px;
  border: 35px solid #fff;
  transform: translate(calc(50vw - 217px), calc(50vh - 225px));
  animation: switch-left-animation 1.75s ease;
}

.pad-left {
  position: fixed;
  width: 80px;
  height: 80px;
  background: #fff;
  border-radius: 100%;
  margin-top: 50px;
  margin-left: 27.5px;
}

.switch-right {
  position: fixed;
  background: #fff;
  width: 185px;
  height: 450px;
  border-radius: 5px 50px 150px 5px;
  transform: translate(calc(50vw + 17px), calc(50vh - 225px));
  animation: switch-right-animation 1.75s ease;
}

.pad-right {
  position: fixed;
  width: 80px;
  height: 80px;
  background: #279690;
  border-radius: 100%;
  margin-top: 225px;
  margin-left: 50px;
}

.line {
  width: 6px;
  height: 100vh;
  position: fixed;
  background: white;
  top: 0;
  left: calc(50vw - 3px);
  opacity: 0.25;
}

.nintendo-text {
  font-family: logofont;
  font-size: 80px;
  color: #fff;
  letter-spacing: 19px;
  position: fixed;
  transform: translate(calc(50vw - 288px), calc(55vh + 175px));
}

.switch-text {
  font-family: logofont;
  font-size: 124px;
  color: #fff;
  letter-spacing: 13px;
  position: fixed;
  transform: translate(calc(50vw - 290px), calc(60vh + 200px));
}

.text {
  animation: text-animation 1.75s ease;
  position: fixed;
}

.clack-svg {
  width: 150px;
  height: 150px;
  background: rgba(255,255,255,0);
  position: fixed;
  transform: translate(calc(50vw + 125px), calc(50vh - 315px)) rotate(-5deg);
  animation: bodyclack 1.75s ease;
}

.clack-svg > line {
  stroke: #fff;;
  stroke-width: 7;
  stroke-dasharray: 100;
  stroke-dashoffset: -100;
  opacity: 0;
  animation: clack 1.75s linear;
}

.reload {
  position: fixed;
  width: 75px;
  height: 75px;
  border-radius: 5px;
  left: calc(50vw - 37.5px);
  bottom: calc(50vh - 345px);
  cursor: pointer;
  transition: background 0.3s ease;
  animation: reload-animation 2.5s ease;
}

.reload:hover {
  background: rgba(0,0,0,0.1)
}

.reload > path {
  fill: #fff;
}

@-webkit-keyframes switch-left-animation {
  0% {transform: translate(calc(50vw - 217px), calc(50vh - 225px));}
  73% {transform: translate(calc(50vw - 217px), calc(50vh - 225px));}
  85% {transform: translate(calc(50vw - 217px), calc(50vh - 195px));}
}

@-webkit-keyframes switch-right-animation {
  0% {transform: translate(calc(50vw + 17px), calc(50vh - 310px));}
  25% {transform: translate(calc(50vw + 17px), calc(50vh - 310px));}
  50% {transform: translate(calc(50vw + 17px), calc(50vh - 325px));}
  65% {transform: translate(calc(50vw + 17px), calc(50vh - 325px));}
  85% {transform: translate(calc(50vw + 17px), calc(50vh - 195px));}
}

@-webkit-keyframes text-animation {
  0% {transform: translate(0px, 0px); opacity:0;}
  70% {}
  75% {transform: translate(0px, 0px);opacity: 0;}
  85% {transform: translate(0px, 15px);}
}

@-webkit-keyframes clack {
  0% {stroke-dashoffset: 100;}
  75% {stroke-dashoffset: 100; opacity: 0;}
  83% {opacity: 1}
  87% {stroke-dashoffset: 0;}
  93% {opacity: 1;}
  100% {stroke-dashoffset: -100; opacity: 0;}
}

@-webkit-keyframes reload-animation {
  0% {opacity: 0;}
  75% {opacity: 0;}
}

@media screen and (max-width: 720px) {
  .logo {
    transform: scale(0.3);
    margin-top: 60px;
  }
}

@media screen and (max-width: 480px) {
  .logo {
    transform: scale(0.5);
    margin-top: 45px;
  }
}

@media screen and (max-height: 420px) {
  .logo {
    transform: scale(0.45);
    margin-top: 65px;
  }
}
.circle {
  position: absolute;
  top:93%;
  left: 50%;
  transform: translate(-50%,-50%);
  width: 43px;
  height: 43px;
  background: rgb(243, 236, 236);
  border: 5px solid 4985s;
  box-shadow: 0 3px 10px 5px  #a8cdd8 50%;
  border-radius: 50%;
  overflow: hidden;
}
.wave {
  position: relative;
  height: 100%;
  width: 100%;
  background: #37aef3;
  border-radius: 50%;
  box-shadow: inset 0 0 50px rgba(0,0,0,.50);
  box-shadow: 0 0 0 4px  #a1a0a0, 0 0 0 5px #cacaca,inset 0 0 10px rgb(167, 164, 164), 0 5px 20px rgba(0,0,0,5), inset 0 0 15px rgba(0,0,0,.2);
}
.wave:before,
.wave:after
{
content: '';
position: absolute;
width: 200%;
height:200%;
top: 0;
left: 50%;
transform: translate(-50%,-75%);

}
.wave:before
{
border-radius: 45%;
background: rgba(255,255,255,1);
animation: animate 5s linear infinite;
box-shadow: 0 0 2px #49c1f8,0 0 0 4px  #949494, 0 0 0 5px #9b9a9a,inset 0 0 10px rgb(22, 22, 22), 0 5px 20px rgba(0,0,0,5), inset 0 0 15px rgba(0,0,0,.2);

}
.wave:after
{
border-radius: 40%;
background: rgba(255,255,255,.5);
animation: animate 5s linear infinite;
}

@keyframes animate
 {
0%
{
transform: translate(-50%,-75%) rotate(100deg);
}
100%
{
transform: translate(-50%,-75%) rotate(360deg);
}
}
.container-login {
  height: 100vh;
  display: flex;
  flex-flow: column;
}

.header-login {
  width: 100%;
  background: #023246ef;
  border-bottom-style: solid;
  border-bottom-width: thick;
  border-bottom-color: #3fb3a4;
}

.header-login-box a {
  text-decoration: none;
  color: #fff;
  font-family: serif;
}
#register {
  padding: 5px 150px;
  display: flex;
}
#forgetpassword {
  padding: 5px 150px;
  display: flex;
}

.header-login-box a:hover {
  color: #3fa5b3;
}

.header-login-box {
  display: flex;
  padding: 15px 250px;
}

.header-text-position {
  flex: auto;
}

.login-box {
  display: flex;
  justify-content: center;
  top: 30%;
  position: sticky;
  animation: box-login 5s;
}

@keyframes box-login {
  0% {
    transform: rotateY(100deg);
  }

  50%,
  100% {
    transform: rotateY(0deg);
  }
}

.login {
  display: flex;
  flex-direction: column;
  width: 370px;
  padding: 20px;
  background-image: linear-gradient(-218deg, #bfe7f3 50%, #a6dcf1 66%);
  border-radius: 15px;
  box-shadow: 0 0 3px #0b012185, 0 0 5px #0b012185, 0 0 15px #0b012185,
    0 0 40px #0b012185;
}

.login h1 {
  text-align: center;
  font-size: 26px;
  padding: 20px;
  color: rgb(141, 139, 139);
}

.login input {
  display: inherit;
  flex-direction: inherit;
  padding: 10px;
}

.login-input-icon {
  position: relative;
  align-self: flex-end;
  top: -38px;
  right: 15px;
  color: #3fa2b3;
  display: block;
}

::placeholder {
  color: rgb(116, 114, 114);
}

.login input[type="text"],
input[type="password"] {
  margin-bottom: 1em;
  background: rgba(29, 2, 2, 0);
  border-bottom-style: solid;
  border-bottom-width: thin;
  border-bottom-color: #155174;
  border-radius: 15px;
  color: rgb(15, 1, 1);
  animation: login-input-focus-initial 1s normal forwards;
  padding-right: 30px;
}

.login input[type="text"]:focus,
input[type="password"]:focus {
  animation: login-input-focus 1s normal forwards;
}

.login-remember {
  display: flex;
  margin-bottom: 1em;
  align-items: center;
}

.login-remember-text {
  align-self: flex-start;
  font-family: serif;
  color: rgb(96, 110, 110);
}

.login-checkbox {
  color: rgb(136, 136, 136);
  width: 15px;
  height: 15px;
  display: inherit;
}

.login-checkbox input {
  cursor: pointer;
  display: none;
}

.checkmark {
  position: relative;
  height: 15px;
  width: 15px;
  background: #fff;
  cursor: pointer;
  border-radius: 5px;
}

.login input:checked ~ .checkmark {
  background-color: #95e4d0 92%;
}

.checkmark:after {
  content: "";
  display: none;
}

.login-checkbox input:checked ~ .checkmark:after {
  display: block;
}

.login .checkmark:after {
  left: 5px;
  top: 2px;
  width: 3px;
  height: 5px;
  border: solid rgb(189, 199, 245);
  border-width: 0 3px 3px 0;
  transform: rotate(45deg);
  position: relative;
}

.login button {
  cursor: pointer;
  padding: 20px;
  border-radius: 15px;
  font-weight: 700;
  color: #fff;
  background-image: linear-gradient(-218deg, #3f92b3 70%, #abe7ff 92%);
  animation: login-button 1s normal forwards;
}

.login button:hover {
  background-image: linear-gradient(-218deg, #2d898f 70%, #95e4d0 92%);
  animation: login-button-hover 1s normal forwards;
}

.login-social-media {
  display: inherit;
  justify-content: center;
  margin-top: 38px;
}

.login-social-media img {
  padding: 0 5px;
  cursor: pointer;
}

.login-separator {
  width: 70%;
  margin: auto;
  height: 2px;
  background: #3fa5b3;
  margin-top: 30px;
}

@keyframes login-input-focus-initial {
  0% {
    font-size: 12px;
  }

  50%,
  100% {
    font-size: 14px;
  }
}

@keyframes login-input-focus {
  0% {
    font-size: 14px;
  }

  50%,
  100% {
    font-size: 12px;
  }
}

@keyframes login-button {
  0% {
    background-size: 200%;
  }

  50%,
  100% {
    background-size: 100%;
  }
}

@keyframes login-button-hover {
  0% {
    background-size: 100%;
  }

  50%,
  100% {
    background-size: 200%;
  }
}
.hello-parent {
  display: flex;
  background: #fff;
  background: -webkit-radial-gradient(#fff, #eaeaea); 
  background: -o-radial-gradient(#fff, #eaeaea); 
  background: -moz-radial-gradient(#fff, #eaeaea);
  background: radial-gradient(#fff, #eaeaea); 
}

.hello-word {
  margin:auto;
}
/* H Animation */

.H-left-stroke {
  stroke-dasharray: 124px;
  stroke-dashoffset: 124px;
  animation: H-left-move 20s ease forwards;
}

.H-mid-stroke {
  stroke-dasharray: 37px;
  stroke-dashoffset: 37px;
  animation: H-mid-move 9s ease forwards;
}

.H-right-stroke {
  stroke-dasharray: 124px;
  stroke-dashoffset: 124px;
  animation: H-right-move 13s ease forwards;
}

@keyframes H-left-move {
  0% {
    stroke-dashoffset: 124px;
  }
  5% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

@keyframes H-mid-move {
  0% {
    stroke-dashoffset: 37px;
  }
  5% {
    stroke-dashoffset: 37px;
  }
  10% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

@keyframes H-right-move {
  0% {
    stroke-dashoffset: 124px;
  }
  5% {
    stroke-dashoffset: 124px;
  }
  10% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

/* E Animation */

.E-left-stroke {
  stroke-dasharray: 124px;
  stroke-dashoffset: 124px;
  animation: E-left-move 20s ease forwards;
}

.E-top-stroke {
  stroke-dasharray: 47px;
  stroke-dashoffset: 47px;
  animation: E-top-move 10s ease forwards;
}

.E-mid-stroke {
  stroke-dasharray: 42px;
  stroke-dashoffset: 42px;
  animation: E-mid-move 10s ease forwards;
}

.E-bottom-stroke {
  stroke-dasharray: 47px;
  stroke-dashoffset: 47px;
  animation: E-bottom-move 10s ease forwards;
}

@keyframes E-left-move {
  0% {
    stroke-dashoffset: 124px;
  }
  2% {
    stroke-dashoffset: 124px;
  }
  6% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

@keyframes E-top-move {
  0% {
    stroke-dashoffset: 47px;
  }
  6% {
    stroke-dashoffset: 47px;
  }
  11% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

@keyframes E-mid-move {
  0% {
    stroke-dashoffset: 42px;
  }
  8% {
    stroke-dashoffset: 42px;
  }
  13% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

@keyframes E-bottom-move {
  0% {
    stroke-dashoffset: 47px;
  }
  11% {
    stroke-dashoffset: 47px;
  }
  16% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

/* L One Animation */

.L-one-long-stroke {
  stroke-dasharray: 124px;
  stroke-dashoffset: 124px;
  animation: L-one-long-move 20s ease forwards;
}

.L-one-short-stroke {
  stroke-dasharray: 44px;
  stroke-dashoffset: 44px;
  animation: L-one-short-move 10s ease forwards;
}

@keyframes L-one-long-move {
  0% {
    stroke-dashoffset: 124px;
  }
  2% {
    stroke-dashoffset: 124px;
  }
  7% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

@keyframes L-one-short-move {
  0% {
    stroke-dashoffset: 44px;
  }
  13% {
    stroke-dashoffset: 44px;
  }
  18% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

/* L Two Animation */

.L-two-long-stroke {
  stroke-dasharray: 124px;
  stroke-dashoffset: 124px;
  animation: L-two-long-move 20s ease forwards;
}

.L-two-short-stroke {
  stroke-dasharray: 44px;
  stroke-dashoffset: 44px;
  animation: L-two-short-move 10s ease forwards;
}

@keyframes L-two-long-move {
  0% {
    stroke-dashoffset: 124px;
  }
  3% {
    stroke-dashoffset: 124px;
  }
  8% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

@keyframes L-two-short-move {
  0% {
    stroke-dashoffset: 44px;
  }
  15% {
    stroke-dashoffset: 44px;
  }
  20% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

/* O Animation */

.O-stroke {
  stroke-dasharray: 302px;
  stroke-dashoffset: 302px;
  animation: O-move 20s ease forwards;
}

@keyframes O-move {
  0% {
    stroke-dashoffset: 302px;
  }
  4% {
    stroke-dashoffset: 302px;
  }
  9% {
    stroke-dashoffset: 0px;
  }
  100% {
    stroke-dashoffset: 0px;
  }
}

/* Red Dot Animation */

.red-dot {
  stroke-width: 44px;
  stroke-linecap: round;
  animation: red-dot-grow 8s ease-out forwards;
}

@keyframes red-dot-grow {
  0% {
    stroke-width: 0px;
  }
  15% {
    stroke-width: 0px;
  }
  20% {
    stroke-width: 44px;
  }
  100% {
    stroke-width: 44px;
  }
}
</style>
