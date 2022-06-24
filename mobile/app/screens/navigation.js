import { StatusBar } from 'expo-status-bar';
import React, { Component } from 'react';
import { StyleSheet, Text, TextInput, TouchableOpacityBase, View, TouchableOpacity, Button } from 'react-native';
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator, HeaderBackButton } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Header } from 'react-native/Libraries/NewAppScreen';
import { enableScreens } from 'react-native-screens';
import Ionicons from 'react-native-vector-icons/Ionicons';

import Login from './LoginScreen';
import Register from './RegisterScreen';
import ConfigService from './ConfigServiceScreen';
import Service from './ServiceScreen';

enableScreens();
const Stack = createStackNavigator();


export default function Navigator() {
  return (
      <NavigationContainer>
        <Stack.Navigator
        screenOptions={{
            gestureEnabled: false,
            headerShown: false,
          }}
        >
          <Stack.Screen
            name='Login'
            component={Login}/>
          <Stack.Screen
            name='Register'
            component={Register}/>
          <Stack.Screen
            name='ConfigService'
            component={ConfigService}/>
          <Stack.Screen
          name='Service'
          component={Service}/>
        </Stack.Navigator>
    </NavigationContainer>
  );
}