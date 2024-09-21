import React from 'react';
import { View, Text, StyleSheet, FlatList, Image ,TouchableOpacity} from 'react-native';
import { icons } from '../constants';
import { Route } from '@react-navigation/native';
import { router } from 'expo-router';
import Link from '@react-navigation/native';


const carChoices = [
  { id: '1', type: 'Bus', destination: 'Church Street', distance:  '44 km', time: '45 mins', cost: '₹412',image: icons.suv },
  { id: '4', type: 'Metro', destination: 'Church Street', distance:  '44 km', time: '50 mins', cost: '₹519',image:icons.suv },
  { id: '2', type: 'Bus', destination: 'Church Street', distance: '44 km', time: '50 mins', cost: '₹590',image: icons.suv},
  { id: '3', type: 'Train', destination: 'Church Street', distance:   '44 km', time: '55 mins', cost: '₹1,009',image: icons.suv },
];

const CarList = () => {

  return (
    <View style={styles.container}>
      <FlatList
        data={carChoices}
        renderItem={({ item }) => (
          <View style={styles.itemContainer}>
            <TouchableOpacity
            style={styles.itemContainer}
            onPress={() => router.replace('confirm')}
          >
            <Text style={styles.itemType}>{item.type}</Text>
            <Image source={item.image} style={styles.icons} />
            <Text style={styles.itemDetail}>Destination: {item.destination}</Text>
            <Text style={styles.itemDetail}>Distance: {item.distance}</Text>
            <Text style={styles.itemDetail}>Expected Time: {item.time}</Text>
            <Text style={styles.itemDetail}>Expected Cost: {item.cost}</Text>
            <View style={styles.separator} />
            

            </TouchableOpacity>
          </View>
        )}
        keyExtractor={(item) => item.id}
      />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    padding: 20,
    backgroundColor: '#f0f4f8',
    marginTop:30,
  },
  icons: {
    width: 30,
    height: 30,
    marginVertical: 5,
  },
  itemContainer: {
    padding: 15,
    backgroundColor: '#fff',
    borderRadius: 8,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 5,
    elevation: 3,
  },
  itemType: {
    fontSize: 18,
    fontFamily: 'Poppins-SemiBold',
    color: '#333',
    marginBottom: 5,
  },
  itemDetail: {
    fontSize: 14,
    fontFamily: 'Poppins-Regular',
    color: '#555',
    marginTop: 2,
  },
  separator: {
    borderBottomWidth: 1,
    borderBottomColor: '#ddd',
    marginVertical: 10,
  },
});

export default CarList;
