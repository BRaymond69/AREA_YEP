import { StatusBar } from 'expo-status-bar';
import React, { Component } from 'react';
import { Text, View, ImageBackground, Image, TextInput, TouchableOpacity } from 'react-native';
import { LoginStyle } from './Style.js';
import Icon from 'react-native-vector-icons/Ionicons';

import BackgroundImage from './assets/backgroundImage.png';
import Logo from './assets/favicon.png';

export default class App extends Component {
  constructor() {
    super()
    this.state = {
      showPass: true,
      press: false
    }
  }

  showPass = () => {
    if (this.state.press == false)
      this.setState({ showPass: false, press: true })
    else
      this.setState({ showPass: true, press: false })
  }

  render() {
    return (
      <ImageBackground source={BackgroundImage} style={LoginStyle.backgroundImage}>

        <View style={LoginStyle.logoContainer}>
          <Image source={Logo} style={LoginStyle.logo} />
          <Text style={LoginStyle.logoText}>Year-End Project - AREA</Text>
        </View>

        <View style={LoginStyle.inputContainer}>
          <Icon name={'ios-person-outline'} size={28} color={'rgba(255, 255, 255, 0.7)'}
            style={LoginStyle.inputIcon} />
          <TextInput
            style={LoginStyle.input}
            placeholder={"Username"}
            placeholderTextColor={'rgba(255,255,255,0.7)'}
            underlineColorAndroid="transparent"
          />
        </View>

        <View style={LoginStyle.inputContainer}>
          {/* <Icon name={'ios-lock-closed-outline'} size={28} color={'rgba(255, 255, 255, 0.7)'}
            style={LoginStyle.inputIcon} /> */}
            <Icon name={this.state.press == false ? 'ios-lock-closed-outline' : 'ios-lock-open-outline'}
              size={28} color={'rgba(255, 255, 255, 0.7)'} style={LoginStyle.inputIcon} />
          <TextInput
            style={LoginStyle.input}
            placeholder={"Password"}
            secureTextEntry={this.state.showPass}
            placeholderTextColor={'rgba(255,255,255,0.7)'}
            underlineColorAndroid="transparent"
          />

          <TouchableOpacity style={LoginStyle.eyeBtn}
            onPress={this.showPass.bind(this)}>
            <Icon name={this.state.press == false ? 'ios-eye-outline' : 'ios-eye-off-outline'} 
              size={26} color={'rgba(255,255,255,0.7)'}/>
          </TouchableOpacity>
        </View>

        <TouchableOpacity style={LoginStyle.loginBtn}>
          <Text style={LoginStyle.text}>Login</Text>
        </TouchableOpacity>
        
        <View>
          <TouchableOpacity style={LoginStyle.googleIcon}
           onPress={this.GoogleSignIn.bind(this)}>
            <Image source={this.state.press == false ? {GoogleSignInIconNormal} : {GoogleSignInIconPressed}} 
              onPress={this.GoogleSignIn.bind(this)}/>
          </TouchableOpacity>
        </View>
        {/* <Text style={LoginStyle.containerText}>Open up App.js to start working on your app!</Text> */}
      </ImageBackground>
    );
  }
}
