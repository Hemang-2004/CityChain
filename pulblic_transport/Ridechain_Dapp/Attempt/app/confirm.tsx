import React from 'react';
import {useState} from 'react'
import { View, Text, StyleSheet, Image } from 'react-native';
import { Ionicons } from '@expo/vector-icons'; // Import icons for checkmark

const RideBookedScreen = () => {
  // Assuming PNR and other details are passed via route parameters
  const pnr = useState("142345");

  return (
    <View style={styles.container}>
      {/* Success Icon */}
      <View style={styles.iconContainer}>
        <Ionicons name="checkmark-circle" size={80} color="#4CAF50" />
      </View>
      
      {/* Success Message */}
      <Text style={styles.successText}>Ride Booked Successfully!</Text>

      {/* PNR Details */}
      <View style={styles.detailsContainer}>
        <Text style={styles.label}>PNR:</Text>
        <Text style={styles.pnrText}>{pnr}</Text>
      </View>

      {/* Thank You Message */}
      <Text style={styles.thankYouText}>Thank you for choosing City Chain!</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FFFFFF', // White background
    padding: 20,
  },
  iconContainer: {
    marginBottom: 20,
  },
  successText: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#000000', // Black text
    marginBottom: 20,
  },
  detailsContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 20,
  },
  label: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#000000', // Black text
  },
  pnrText: {
    fontSize: 18,
    color: '#000000', // Black text
    marginLeft: 10,
  },
  thankYouText: {
    fontSize: 18,
    color: '#000000', // Black text
    textAlign: 'center',
  },
});

export default RideBookedScreen;
