import { Text, TextInput, View } from "react-native"
import { ScrollView } from "react-native"

function signup() {
  return (
    <ScrollView>
        <View>
            <Text>Create Account</Text>
            <Text>Create a new account to get started</Text>

            <Text>Fill the address details</Text>

            <View>
              <View>
                <Text></Text>
                <TextInput />
              </View>
              <View>
                <Text></Text>
                <TextInput />
              </View>
              <View>
                <Text></Text>
                <TextInput />
              </View>
              <View>
                <Text></Text>
                <TextInput />
              </View>
              <View>
                <Text></Text>
                <TextInput />
              </View>
            </View>
        </View>
    </ScrollView>
  )
}

export default signup