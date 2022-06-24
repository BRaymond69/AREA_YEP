import React, { Component } from 'react';
import { ImageBackground, StyleSheet, View, Dimensions, Image, ScrollView, Text, Button, Alert } from 'react-native';
import { TextInput } from 'react-native-gesture-handler';

class CardScreen extends Component {
  constructor(props) {
    super(props);
    this.state = {
      username: '',
      password: '',
    };
  }
  render() {
    return (
      <View>
      </View>
    )
  }
}
const styles = StyleSheet.create({
  background: {
    flex: 1,
    justifyContent: "flex-end",
  },
  
})
export default CardScreen;