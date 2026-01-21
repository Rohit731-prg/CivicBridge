import {
  Image,
  Pressable,
  ScrollView,
  StyleSheet,
  Text,
  View,
} from "react-native";

function Home() {
  return (
    <ScrollView style={style.container}>
      <View style={style.header}>
        <View>
          <Pressable>
            <Text style={style.main_text}>Call</Text>
          </Pressable>
          <Image
            height={50}
            width={50}
            source={{
              uri: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg801d3QPVE9bwG7y_TaYO2--IOeOwdrYq9g&s",
            }}
          />
          <Pressable>
            <Text style={style.main_text}>Call</Text>
          </Pressable>
        </View>

        <View style={style.parant_mini_con}>
          <View style={style.mini_container}>
            <Text style={[style.main_text, style.text]}>Total Complains</Text>
            <Text style={[style.main_text, style.text]}>4</Text>
          </View>
          <View style={style.mini_container}>
            <Text style={[style.main_text, style.text]}>Total Complains</Text>
            <Text style={[style.main_text, style.text]}>4</Text>
          </View>
        </View>
      </View>
      <View style={style.main}>
        <Pressable style={style.main_btn}>
          <Text style={style.main_text}>Emergency</Text>
        </Pressable>
      </View>
    </ScrollView>
  );
}

const style = StyleSheet.create({
  container: {
    width: "100%",
    flex: 1,
    padding: 10,
    paddingVertical: 40
  },
  header: {
    backgroundColor: "#331ef7",
    borderRadius: 10,
    elevation: 5,
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    flexDirection: "column",
    marginBottom: 20,
    padding: 20
  },

  main: {
    paddingHorizontal: 10,
    paddingVertical: 80,
    backgroundColor: "white",
    borderRadius: 10,
    elevation: 5,
    marginHorizontal: 10,
    display: "flex",
    alignItems: "center",
    justifyContent: "center"
  },
  main_btn: {
    width: 100,
    height: 100,
    backgroundColor: "red",
    display: "flex",
    alignItems: "center",
    justifyContent: "center",
    borderRadius: 999,
    elevation: 20,
  },
  main_text: {
    color: "white",
    fontWeight: 600
  },
  mini_container: {
    padding: 20,
    backgroundColor: "white",
    borderRadius: 10,
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    marginHorizontal: 10
  },
  text: {
    color: "black"
  },
  parant_mini_con: {
    display: "flex",
    flexDirection: "row",
  }
});

export default Home;
