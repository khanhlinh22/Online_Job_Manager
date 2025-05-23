import { StyleSheet } from "react-native";

export default StyleSheet.create({
  container: {
    flex: 1,
    // justifyContent: "center", // SAI chính tả trước là "jusifyContent"
    // alignItems: "center"
  }, row:{
    flexDirection: "row",
    flexWrap: "wrap"
  }, margin: {
    margin: 5
  },
  subject: {
    fontSize: 25,             // SAI chính tả: "fontsize" -> đúng là "fontSize"
    color: "blue",
    fontWeight: "bold"        // SAI: "fontHeight" -> đúng là "fontWeight"
  }
});
