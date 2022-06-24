import { StatusBar } from 'expo-status-bar';
import React, { Component } from 'react';
import { StyleSheet, Text, TextInput, TouchableOpacityBase, View, TouchableOpacity, Button } from 'react-native';
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator, HeaderBackButton } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Login from './app/screens/LoginScreen';
import Register from './app/screens/RegisterScreen';
import Navigator from './app/screens/navigation'
import { Header } from 'react-native/Libraries/NewAppScreen';
import { enableScreens } from 'react-native-screens';
import Ionicons from 'react-native-vector-icons/Ionicons';
import './global.js'

enableScreens();
const Tab = createBottomTabNavigator();
const Stack = createStackNavigator();


export default function App() {
  return (
    <Navigator/>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
