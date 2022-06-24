import { StatusBar } from 'expo-status-bar';
import React, { useEffect, useState, Component } from 'react';
import { Text, View, ImageBackground, Image, TextInput, TouchableOpacity, AsyncStorage } from 'react-native';
import { LoginStyle } from './Styles/Style.js';
import Icon from 'react-native-vector-icons/Ionicons';
import * as API from './../api/api'
import * as AppAuth from 'expo-app-auth';
import { Ionicons } from '@expo/vector-icons';
import BackgroundImage from './assets/backgroundImage.png';
import Logo from './assets/favicon.png';

export default function LoginScreen(props) {
  const { navigation } = props
  let [authState, setAuthState] = useState(null);
  let [username, usernameInput] = useState(null);
  let [password, passwordInput] = useState(null);
  useEffect(() => {
    (async () => {
      let cachedAuth = await getCachedAuthAsync();
      if (cachedAuth && !authState) {
        setAuthState(cachedAuth);
      }
    })();
  }, []);
  loginBody = async () => {
    const body = new FormData();
    if (username != "" && password != "") {
      body.append('username', username)
      body.append('password', password)
      console.log(`${global.ngrokLink}/login/`)
      API.loginServer(`${global.ngrokLink}/login/`, body, navigation)
    }
  }
  loginGoogleBody = async () => {
    const body = new FormData();
    if (username != "" && password != "") {
      body.append('googleToken', global.googleToken)
      API.loginServerGoogle(`${global.ngrokLink}/googleregister/`, body, navigation)
    }
  }
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
          autoCapitalize="none"
          value={username}
          onChangeText = {text => usernameInput(text)}
        />
      </View>
      <View style={LoginStyle.inputContainer}>
        {/* <Icon name={'ios-lock-closed-outline'} size={28} color={'rgba(255, 255, 255, 0.7)'}
          style={LoginStyle.inputIcon} /> */}
          <Icon name={'ios-lock-open-outline'}
            size={28} color={'rgba(255, 255, 255, 0.7)'} style={LoginStyle.inputIcon} />
        <TextInput
          style={LoginStyle.input}
          placeholder={"Password"}
          secureTextEntry={true}
          placeholderTextColor={'rgba(255,255,255,0.7)'}
          underlineColorAndroid="transparent"
          autoCapitalize="none"
          value={password}
          onChangeText = {text => passwordInput(text)}
        />
      </View>
      <View style={LoginStyle.viewBtn}>
        <TouchableOpacity style={LoginStyle.loginBtn} onPress={loginBody}>
          <Text style={LoginStyle.text}>Login</Text>
        </TouchableOpacity>
        <TouchableOpacity style={LoginStyle.loginBtn} onPress={() => navigation.navigate('Register')}>
          <Text style={LoginStyle.text}>Register</Text>
        </TouchableOpacity>
      </View>
      <Ionicons
        style={{textAlign: 'center', paddingTop:10}}
        name="logo-google"
        size={44}
        color="blue"
        onPress={async () => {
          const _authState = await signInAsync();
          setAuthState(_authState);
          loginGoogleBody();
        }}
      />
      {/* <Text style={LoginStyle.containerText}>Open up App.js to start working on your app!</Text> */}
    </ImageBackground>
  );
}

let config = {
  issuer: 'https://accounts.google.com',
  scopes: ['openid', 'profile'],
  clientId: '603386649315-vp4revvrcgrcjme51ebuhbkbspl048l9.apps.googleusercontent.com',
};

let StorageKey = '@MyApp:CustomGoogleOAuthKey';

export async function signInAsync() {
  let authState = await AppAuth.authAsync(config);
  await cacheAuthAsync(authState);
  global.googleToken = authState.idToken;
  return authState;
}

async function cacheAuthAsync(authState) {
  return await AsyncStorage.setItem(StorageKey, JSON.stringify(authState));
}

export async function getCachedAuthAsync() {
  let value = await AsyncStorage.getItem(StorageKey);
  let authState = JSON.parse(value);
  if (authState) {
    if (checkIfTokenExpired(authState)) {
      return refreshAuthAsync(authState);
    } else {
      return authState;
    }
  }
  return null;
}


function checkIfTokenExpired({ accessTokenExpirationDate }) {
  return new Date(accessTokenExpirationDate) < new Date();
}


async function refreshAuthAsync({ refreshToken }) {
  let authState = await AppAuth.refreshAsync(config, refreshToken);
  await cacheAuthAsync(authState);
  return authState;
}

export async function signOutAsync({ accessToken }) {
  try {
    await AppAuth.revokeAsync(config, {
      token: accessToken,
      isClientIdProvided: true,
    });
    await AsyncStorage.removeItem(StorageKey);
    return null;
  } catch (e) {
    alert(`Failed to revoke token: ${e.message}`);
  }
}