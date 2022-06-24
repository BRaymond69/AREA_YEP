import React, { Component } from 'react';
import { Text, View, FlatList, TouchableOpacity, Image, ScrollView, TextInput} from 'react-native';
import { ServiceStyle } from './Styles/ServiceStyle.js';
import Icon from 'react-native-vector-icons/Ionicons';
import { LoginStyle } from './Styles/Style.js';
import * as API from '../api/api'
import Icons from 'react-native-vector-icons/MaterialIcons';

function Item({ item }) {
  return (
      <View style={ServiceStyle.listItem}>
          <Image source={{ uri: item.photo }} style={{ width: 60, height: 60, borderRadius: 30 }} />
          <View style={{ alignItems: "center", flex: 1 }}>
              <Text style={{ fontWeight: "bold" }}>{item.name}</Text>
              <Text>{item.position}</Text>
          </View>
      </View>
  );
}

export default class ServiceScreen extends Component {  
  constructor(props) {
    super(props);
    this.state = {
      data: [
        {
          "id": 0,
          "name": "not configured",
          "photo": "https://www.leparisien.fr/resizer/d215pck3D75_RttKY8bvRIoEzVw=/932x582/cloudfront-eu-central-1.images.arcpublishing.com/leparisien/AJNGNE3DZE2424T3T3KNPTZFB4.jpg",
          "activated": false
        },
        {
          "id": 1,
          "name": "not configured",
          "photo": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADMAAAAzCAYAAAA6oTAqAAAAEXRFWHRTb2Z0d2FyZQBwbmdjcnVzaEB1SfMAAABQSURBVGje7dSxCQBACARB+2/ab8BEeQNhFi6WSYzYLYudDQYGBgYGBgYGBgYGBgYGBgZmcvDqYGBgmhivGQYGBgYGBgYGBgYGBgYGBgbmQw+P/eMrC5UTVAAAAABJRU5ErkJggg==",
          "activated": false
        },
        {
          "id": 2,
          "name": "not configured",
          "photo": "https://yt3.ggpht.com/ytc/AAUvwni_LdnpDi-SOIhjp4Kxo2l_yVBoYsfdDCpUM5VDzg=s900-c-k-c0x00ffffff-no-rj",
          "activated": false
        },
        {
          "id": 3,
          "name": "not configured",
          "photo": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/14/Blu-ray_Disc.svg/1200px-Blu-ray_Disc.svg.png",
          "activated": false
        },
        {
          "id": 4,
          "name": "not configured",
          "position": "not configured",
          "photo": "https://f.hellowork.com/blogdumoderateur/2019/11/twitter-logo-1200x1200.jpg",
          "activated": false
        },
        {
          "id": 5,
          "name": "not configured",
          "photo": "https://eip.epitech.eu/2013/gns3/images/epitech.png",
          "activated": false
        },
      ]
    }
  }
  componentDidMount(){
    this.requestServices();
  }
  logout = async () => {
    API.logoutServer(`${global.ngrokLink}/logout/`)
    this.props.navigation.navigate('Login')
  }
  showConfig = async () => {
    this.props.navigation.navigate('ConfigService')
  }

  // SERVICES REQUEST


  getFilm = async (link, body) => {
    return await fetch(link, {
        method: 'POST',
        headers:  {      
            'Authorization': `Token ${global.connectToken}`
           },
        body: body
    }
    )
    .then(response => response.json())
    .then(response => {
        this.state.data[3].name = `Film incoming : ${response.data.Film[0]}`
        this.forceUpdate();
      }).catch((err) => console.log(err));
};

 getNetflix = async (link, body) => {
    return await fetch(link, {
        method: 'POST',
        headers:  {      
            'Authorization': `Token ${global.connectToken}`
           },
        body: body
    }
    )
    .then(response => response.json())
    .then(response => {
        this.state.data[2].name = `Netflix film incoming : ${response.data}`
        this.forceUpdate();
      }).catch((err) => console.log(err));
};

getAmazon = async (link, body) => {
    return await fetch(link, {
        method: 'POST',
        headers:  {      
            'Authorization': `Token ${global.connectToken}`
           },
        body: body
    }
    )
    .then(response => response.json())
    .then(response => {
        this.state.data[0].name = `Amazon film incoming : ${response.data}`
        this.forceUpdate();
      }).catch((err) => console.log(err));
};


  getIntra = async (link, body) => {
  return await fetch(link, {
      method: 'POST',
      headers:  {
          'Authorization': `Token ${global.connectToken}`
         },
      body: body
  }
  )
  .then(response => response.json())
  .then(response => {
      this.state.data[5].name = response.data
      this.forceUpdate();
    }).catch((err) => console.log(err));
  };

  getTwitch = async (link, body) => {
  return await fetch(link, {
      method: 'POST',
      headers:  {      
          'Authorization': `Token ${global.connectToken}`
         },
      body: body
  }
  )
  .then(response => response.json())
  .then(response => {
      this.state.data[1].photo = response.data["url photo"]
      this.state.data[1].name = `${response.data.Streamer} is in live: ${response.data.is_live}`
      this.forceUpdate();
    }).catch((err) => console.log(err));
  };

  getTwitter = async (link, body) => {
  return await fetch(link, {
      method: 'POST',
      headers:  {      
          'Authorization': `Token ${global.connectToken}`
         },
      body: body
  }
  )
  .then(response => response.json())
  .then(response => {
    this.state.data[4].name = `${response.data.Author}`
    this.state.data[4].position = `       ${response.data.Text}`
    this.forceUpdate();
  }).catch((err) => console.log(err));
  };


  //
  requestServices = () => {
    if (global.netflixNumber != "") {
      const bodyNetflix = new FormData();
      bodyNetflix.append('netflixNumber', global.netflixNumber)
      this.getNetflix(`${global.ngrokLink}/netflix/`, bodyNetflix)
    }
    if (global.amazonNumber != "") {
      const bodyAmazon = new FormData();
      bodyAmazon.append('amazonNumber', global.amazonNumber)
      this.getAmazon(`${global.ngrokLink}/amazon/`, bodyAmazon)
    }
    if (global.filmNumber != "") {
      const bodyFilm = new FormData();
      bodyFilm.append('filmNumber', global.filmNumber)
      this.getFilm(`${global.ngrokLink}/film/`, bodyFilm)
    }
    if (global.twitch != "") {
      const bodyTwitch = new FormData();
      bodyTwitch.append('twitchAccount', global.twitch)
      this.getTwitch(`${global.ngrokLink}/twitch/`, bodyTwitch)
    }
    if (global.twitter != "") {
      const bodyTwitter = new FormData();
      bodyTwitter.append('twitterAccount', global.twitter)   
      this.getTwitter(`${global.ngrokLink}/twitter/`, bodyTwitter)
    }
    if (global.idIntra != "") {
      const bodyIntra = new FormData();
      bodyIntra.append('autoToken', global.idIntra)
      this.getIntra(`${global.ngrokLink}/intra/`, bodyIntra)
    }
  }

  render() {
    return (
      <View style={ServiceStyle.backgroundImage}>
        <View style={ServiceStyle.Header}>
          <View style={LoginStyle.viewBtn}>
            <TouchableOpacity style={LoginStyle.logoutBtn} onPress={this.logout}>
              <Text style={LoginStyle.textBlackOnWhite}>LOGOUT</Text>
            </TouchableOpacity>
          </View>
          <Text style={ServiceStyle.logoText}>Services</Text>
        </View>
        <FlatList
            style={{ flex: 1 }}
            data={this.state.data}
            renderItem={({ item }) => <Item item={item} />}
            keyExtractor={item => item.id}
          />
          <Text>{this.state.data[1].photo}</Text>
      <TouchableOpacity style={LoginStyle.Services} onPress={this.showConfig}>
              <Text style={LoginStyle.textBlackOnWhite}>Configure</Text>
            </TouchableOpacity>
      </View>
    );
    }
  }
