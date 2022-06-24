import React, { Component } from 'react';
import { Text, View, FlatList, TouchableOpacity, Image, ScrollView} from 'react-native';
import { ServiceStyle } from './Styles/ServiceStyle.js';
import Icon from 'react-native-vector-icons/Ionicons';
import { LoginStyle } from './Styles/Style.js';
import * as API from './../api/api'


function Item({ item }) {
  return (
      <View style={ServiceStyle.listItem}>
          <Image source={{ uri: item.photo }} style={{ width: 60, height: 60, borderRadius: 30 }} />
          <View style={{ alignItems: "center", flex: 1 }}>
              <Text style={{ fontWeight: "bold" }}>{item.name}</Text>
              <Text>{item.position}</Text>
          </View>
          <TouchableOpacity style={{ height: 50, width: 50, justifyContent: "center", alignItems: "center" }}>
              <Text style={{ color: "green" }}>Call</Text>
          </TouchableOpacity>
      </View>
  );
}

export default function ServiceScreen(props) {
  const { navigation } = props
  showFacebookService = async () => {
    const body = new FormData();
    if (global.isCoFB == "no")
    body.append('token', global.connectToken)
    body.append('email', global.connectToken)
    body.append('password', global.connectToken)
    API.getFB("https://c97dadf06f88.ngrok.io/facebook", global.connectToken)
  }
  showIntraService = async () => {
    API.getIntra("https://c97dadf06f88.ngrok.io/intra/")
  }
  logout = async () => {
    API.logoutServer("https://c97dadf06f88.ngrok.io/logout/")
    navigation.navigate('Login')
  }
return (
    <View style={ServiceStyle.backgroundImage}>
      <View style={ServiceStyle.Header}>
        <Text style={ServiceStyle.logoText}>Choose a service</Text>
      </View>
      <View style={LoginStyle.viewBtn}>
        <TouchableOpacity style={LoginStyle.loginBtn} onPress={this.showIntraService}>
          <Text style={LoginStyle.text}>Intra</Text>
        </TouchableOpacity>
        <TouchableOpacity style={LoginStyle.loginBtn} onPress={loginBody}>
          <Text style={LoginStyle.text}>Facebook</Text>
        </TouchableOpacity>
      </View>
      <View style={LoginStyle.viewBtn}>
        <TouchableOpacity style={LoginStyle.logoutBtn} onPress={this.logout}>
          <Text style={LoginStyle.textBlackOnWhite}>LOGOUT</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}


/*
<FlatList
            style={{ flex: 1 }}
            data={this.state.data}
            renderItem={({ item }) => <Item item={item} />}
            keyExtractor={item => item.id}
          />
          */