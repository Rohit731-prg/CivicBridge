import { Image, Pressable, StyleSheet, Text } from "react-native"
import { ScrollView, View } from "react-native"

function Account() {
    const account_details_list = [
        { id: 1, name: "My Complains", link: ""},
        { id: 2, name: "Emergency History", link: ""},
        { id: 3, name: "Edit Profile", link: ""},
        { id: 4, name: "Saved Addresses", link: ""},
    ];

  return (
    <ScrollView style={style.container}>
        <View>
            <Text>Back</Text>
        </View>

        <View style={style.content}>
            <Image source={{ uri: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTg801d3QPVE9bwG7y_TaYO2--IOeOwdrYq9g&s"}} style={style.image} />
            <View style={style.contentText}>
                <Text>Rohit Singha</Text>
                <Text>+91 9883583218</Text>
            </View>
        </View>
        <Pressable style={style.profile}>
            <Text style={{ color: "white", fontWeight: "bold" }}>View full profile</Text>
        </Pressable>

        <View style={{ marginVertical: 40 }}>
            {account_details_list.map((item) => (
                <Pressable key={item.id} style={style.compo}>
                    <Text style={{ color: "black", fontWeight: "bold", fontSize: 16 }}>
                        {item.name}
                    </Text>
                </Pressable>
            ))}
        </View>

        <Pressable style={style.logout}>
            <Text style={{ color: "white", fontWeight: "bold" }}>LOG OUT</Text>
        </Pressable>
    </ScrollView>
  )
}

const style = StyleSheet.create({
    container: {
        padding: 20,
        paddingVertical: 30,
    },
    content: {
        padding: 5,
        display: "flex",
        flexDirection: "row",
    },
    image: {
        width: 80,
        height: 80,
        borderRadius: 999,
        marginRight: 10,
    },
    contentText: {
        marginTop: 10
    },

    profile: {
        backgroundColor: "#2b41ff",
        padding: 10,
        borderRadius: 5,
        alignItems: "center",
        marginTop: 20,
    },

    compo: {
        paddingVertical: 10,
        borderBottomWidth: 1,
        borderColor: "black",
        borderRadius: 5,
        marginTop: 10,
    },

    logout: {
        backgroundColor: "red",
        padding: 10,
        borderRadius: 5,
        alignItems: "center",
        marginTop: 20,
    }
})

export default Account