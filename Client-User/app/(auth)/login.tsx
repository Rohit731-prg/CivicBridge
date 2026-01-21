import {
  Pressable,
  ScrollView,
  StyleSheet,
  Text,
  TextInput,
  View,
} from "react-native";
import LottieView from "lottie-react-native";
import loading from "../../assets/loading.json";
import { router } from "expo-router";
import { useState } from "react";

function Login() {
  const [loadingBtn, setLoading] = useState<boolean>(false);
  const [userDetails, setUserDetails] = useState({
    phone_number: "",
    password: ""
  });

  const handelSubmit = () => {
    alert("jikjik");
    router.push("/(tabs)/home");
  };
  return (
    <ScrollView contentContainerStyle={styles.container}>
      <View style={styles.animationWrapper}>
        <LottieView source={loading} autoPlay loop style={styles.loading} />
      </View>

      <Text style={styles.title}>Welcome Back</Text>
      <Text style={styles.subtitle}>Login to continue</Text>

      <View style={styles.form}>
        <TextInput
          placeholder="Enter phone number"
          
          placeholderTextColor="#999"
          style={styles.input}
        />

        <TextInput
          placeholder="Enter password"
          placeholderTextColor="#999"
          secureTextEntry
          style={styles.input}
        />

        <Pressable style={styles.btn}  onPress={() => handelSubmit()}>
          <Text style={styles.btnText}>{!loadingBtn ? "SUBMIT" : "Loading..."}</Text>
        </Pressable>
      </View>

      <View style={styles.bottomSection}>
        <Pressable style={styles.emergencyBtn}>
          <Text style={styles.emergencyText}>Emergency Call</Text>
        </Pressable>

        <View style={styles.signupRow}>
          <Text style={styles.signupText}>Don&apos;t have an account?</Text>
          <Pressable>
            <Text style={styles.signupLink} onPress={() => router.push("/(auth)/signup")}> Sign up</Text>
          </Pressable>
        </View>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: {
    flexGrow: 1,
    padding: 24,
    backgroundColor: "#fff",
    justifyContent: "center",
  },

  animationWrapper: {
    alignItems: "center",
    marginBottom: 4,
  },

  loading: {
    width: 260,
    height: 260,
  },

  title: {
    fontSize: 28,
    fontWeight: "700",
    textAlign: "center",
    color: "#111",
  },

  subtitle: {
    fontSize: 14,
    textAlign: "center",
    color: "#666",
    marginBottom: 32,
  },

  form: {
    gap: 16,
  },

  input: {
    height: 50,
    borderWidth: 1,
    borderColor: "#ddd",
    borderRadius: 10,
    paddingHorizontal: 14,
    fontSize: 16,
    color: "#111",
    backgroundColor: "#fafafa",
  },

  btn: {
    width: "100%",
    paddingVertical: 15,
    borderRadius: 10,
    backgroundColor: "#2563EB",
  },

  btnText: {
    color: "#fff",
    textAlign: "center",
    fontWeight: "600",
    fontSize: 16,
  },

  bottomSection: {
    marginTop: 32,
    alignItems: "center",
    gap: 16,
  },

  emergencyBtn: {
    paddingVertical: 12,
  },

  emergencyText: {
    color: "#DC2626",
    fontWeight: "600",
  },

  signupRow: {
    flexDirection: "row",
  },

  signupText: {
    color: "#555",
  },

  signupLink: {
    color: "#2563EB",
    fontWeight: "600",
  },
});

export default Login;
