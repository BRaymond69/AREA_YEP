import React, { useEffect, useState } from 'react';
import { AsyncStorage, Button, StyleSheet, Text, View } from 'react-native';
import * as AppAuth from 'expo-app-auth';
import { Ionicons } from '@expo/vector-icons';
import * as API from './../api/api'
import { TextInput } from 'react-native-gesture-handler';

/*      <Text>{JSON.stringify(authState, null, 2)}</Text>
 
      <Button
        title="Sign Out "
        onPress={async () => {
          await signOutAsync(authState);
          setAuthState(null);
        }}
      /> */


export default function App() {
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
    body.append('username', username)
    body.append('password', password)
    API.connectServer("http://127.0.0.1:8000/login", body)
  }
  return (
    <View
      borderColor="#48376d"
      borderWidth={5}
      width={250}
      style={{textAlign: 'center', display:'flex', marginLeft:60, marginTop:150}}
    >
      <View
        style={{}}
      >
        <Text
          style={{ fontWeight: 'bold', textAlign: 'center', fontSize: 22, borderColor: '#48376d', borderBottomWidth: 5}}>
            Login
        </Text>
      </View>
      <TextInput paddingTop={5} placeholder="Username" autoCapitalize="none" value={username} onChangeText = {text => usernameInput(text)}></TextInput>
      <TextInput paddingBottom={5} secureTextEntry={true} placeholder="Password" autoCapitalize="none" value={password} onChangeText = {text => passwordInput(text)}></TextInput>
      <Button
        padding={10}
        title="log in"
        onPress={loginBody}
      ></Button>
      <Button
        padding={10}
        title="register"
      >
      </Button>
      <Ionicons
        style={{textAlign: 'center', paddingTop:10}}
        name="logo-google"
        size={44}
        color="blue"
        onPress={async () => {
          const _authState = await signInAsync();
          setAuthState(_authState);
        }}
      />
    </View>
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
  global.googleToken = authState.accessToken;
  return authState;
}

async function cacheAuthAsync(authState) {
  return await AsyncStorage.setItem(StorageKey, JSON.stringify(authState));
}

export async function getCachedAuthAsync() {
  let value = await AsyncStorage.getItem(StorageKey);
  let authState = JSON.parse(value);
  //console.log('getCachedAuthAsync', authState);
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
  console.log('refreshAuth', authState);
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

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
  background: {
    flex: 1,
    justifyContent: "flex-end",
  },
  image: {
    resizeMode: "stretch",
    width: "100%",
    height: "auto",
    aspectRatio: 1,
  },
  connectButton: {
    width: 250,
    position: 'relative',
    marginTop: 10,
    marginLeft: 50,
  },
  usernameFields: {
    width: 250,
    position: 'relative',
    borderWidth: 1,
    borderColor: 'black',
    marginTop: 200,
    marginLeft: 50,
  },
  passwordFields: {
    width: 250,
    position: 'relative',
    marginTop: 10,
    marginLeft: 50,
    borderWidth: 1,
    borderColor: 'black',
  },
});
