import React, { Component, useState, useEffect } from 'react';
import { Text, View, FlatList, TouchableOpacity, Image, ScrollView, TextInput} from 'react-native';
import { ServiceStyle } from './Styles/ServiceStyle.js';
import Icon from 'react-native-vector-icons/Ionicons';
import { LoginStyle } from './Styles/Style.js';
import * as API from '../api/api'

export default function ServiceScreen(props) {
  const { navigation } = props
  let [idIntra, setIdIntra] = useState(null);
  let [twitch, setTwitch] = useState(null);
  let [twitter, setTwitter] = useState(null);
  let [emailAddr, setEmailAdress] = useState(null);
  let [emailPassd, setEmailPassword] = useState(null);
  let [news, setNews] = useState(null);
  let [film, setFilm] = useState(null);
  let [netflix, setNetflix] = useState(null);
  let [amazon, setAmazon] = useState(null);
  let [date, setDate] = useState(null);
  let [fbMail, setFbMail] = useState(null);
  let [fbPasswd, setFbpasswd] = useState(null);

  showServices = async () => {
    navigation.navigate('Service')
  }
  logout = async () => {
    API.logoutServer(`${global.ngrokLink}/logout/`)
    navigation.navigate('Login')
  }

  showFacebookService = async () => {
    global.fbMail = fbMail
    global.fbpass = fbPasswd
  }
  showDate = async () => {
    global.date = date
  }
  showAmazon = async () => {
    global.amazonNumber = amazon
  }
  showNetflix = async () => {
    global.netflixNumber = netflix
  }
  showFilm = async () => {
    global.filmNumber = film
  }
  showNews = async () => {
    global.news = news
  }
  postMail = async () => {
    global.email = emailAddr
    global.password = emailPassd
  }
  showTwitter = async () => {
    global.twitter = twitter
  }
  showTwitch = async () => {
    global.twitch = twitch
  }
  showIntraService = async () => {
    global.idIntra = idIntra
  }
return (
    <View style={ServiceStyle.backgroundImage}>
      <View style={ServiceStyle.Header}>

      <View style={LoginStyle.viewBtn}>
        <TouchableOpacity style={LoginStyle.logoutBtn} onPress={this.logout}>
          <Text style={LoginStyle.textBlackOnWhite}>LOGOUT</Text>
        </TouchableOpacity>
      </View>
        <Text style={ServiceStyle.logoText}>Config your services</Text>
      </View>
      <ScrollView style={LoginStyle.scrollView}>
        <View style={LoginStyle.viewConfig}>
          <View style={LoginStyle.inputContainer}>
            <TextInput
              style={LoginStyle.inputConfig}
              placeholder={"auth-xxxxx..."}
              placeholderTextColor={'rgba(255,255,255,0.7)'}
              underlineColorAndroid="transparent"
              autoCapitalize="none"
              value={idIntra}
              onChangeText = {text => setIdIntra(text)}
            />
          </View>
          <TouchableOpacity style={LoginStyle.configBtn} onPress={this.showIntraService}>
              <Text style={LoginStyle.textBlackOnWhite}>Intra</Text>
            </TouchableOpacity>
        </View>
        <View style={LoginStyle.viewConfig}>
          <View style={LoginStyle.inputContainer}>
            <TextInput
              style={LoginStyle.inputConfig}
              placeholder={"Twitch Account in live"}
              placeholderTextColor={'rgba(255,255,255,0.7)'}
              underlineColorAndroid="transparent"
              autoCapitalize="none"
              value={twitch}
              onChangeText = {text => setTwitch(text)}
            />
          </View>
          <TouchableOpacity style={LoginStyle.configBtn} onPress={this.showTwitch}>
              <Text style={LoginStyle.textBlackOnWhite}>Twitch</Text>
            </TouchableOpacity>
        </View>

        <View style={LoginStyle.viewConfig}>
          <View style={LoginStyle.inputContainer}>
            <TextInput
              style={LoginStyle.inputConfig}
              placeholder={"Twitter account"}
              placeholderTextColor={'rgba(255,255,255,0.7)'}
              underlineColorAndroid="transparent"
              autoCapitalize="none"
              value={twitter}
              onChangeText = {text => setTwitter(text)}
            />
          </View>
          <TouchableOpacity style={LoginStyle.configBtn} onPress={this.showTwitter}>
              <Text style={LoginStyle.textBlackOnWhite}>Twitter</Text>
            </TouchableOpacity>
        </View>

        <View style={LoginStyle.viewConfig}>
          <View style={LoginStyle.inputContainer}>
            <TextInput
              style={LoginStyle.inputConfig}
              placeholder={"Number of film upper than 0"}
              placeholderTextColor={'rgba(255,255,255,0.7)'}
              underlineColorAndroid="transparent"
              autoCapitalize="none"
              value={film}
              onChangeText = {text => setFilm(text)}
            />
          </View>
          <TouchableOpacity style={LoginStyle.configBtn} onPress={this.showFilm}>
              <Text style={LoginStyle.textBlackOnWhite}>Film</Text>
            </TouchableOpacity>
        </View>

        <View style={LoginStyle.viewConfig}>
          <View style={LoginStyle.inputContainer}>
            <TextInput
              style={LoginStyle.inputConfig}
              placeholder={"Number of incoming Netflix film upper than 0"}
              placeholderTextColor={'rgba(255,255,255,0.7)'}
              underlineColorAndroid="transparent"
              autoCapitalize="none"
              value={netflix}
              onChangeText = {text => setNetflix(text)}
            />
          </View>
          <TouchableOpacity style={LoginStyle.configBtn} onPress={this.showNetflix}>
              <Text style={LoginStyle.textBlackOnWhite}>Netflix</Text>
            </TouchableOpacity>
        </View>

        <View style={LoginStyle.viewConfig}>
          <View style={LoginStyle.inputContainer}>
            <TextInput
              style={LoginStyle.inputConfig}
              placeholder={"Number of incoming Amazon film upper than 0"}
              placeholderTextColor={'rgba(255,255,255,0.7)'}
              underlineColorAndroid="transparent"
              autoCapitalize="none"
              value={amazon}
              onChangeText = {text => setAmazon(text)}
            />
          </View>
          <TouchableOpacity style={LoginStyle.configBtn} onPress={this.showAmazon}>
              <Text style={LoginStyle.textBlackOnWhite}>Amazon</Text>
            </TouchableOpacity>
        </View>

      </ScrollView>
      <TouchableOpacity style={LoginStyle.Services} onPress={this.showServices}>
              <Text style={LoginStyle.textBlackOnWhite}>Services</Text>
            </TouchableOpacity>
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