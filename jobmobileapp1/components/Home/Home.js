import { View, Text } from "react-native";
import MyStyles from "../../styles/MyStyles";
import { useEffect, useState } from "react";
import APIs, { endpoints } from "../../configs/APIs";
import { ActivityIndicator, Chip } from "react-native-paper";

const Home = () => {
    const [categories, setCategories] = useState([]);
    const [recruitments, setRecruitments] = useState([]);
    const [loading, setLoading] = useState([]);

    const loadCates = async () => {
        let res = await APIs.get(endpoints['categories']);
        console.info(res.data);
        setCategories(res.data.results);
    }

    const loadRecruits = async () => {
        loading(true);

        try{
            let res = await APIs.get(endpoints['recruitments']);
            setRecruitments(res.data.result);
        }
        catch(ex) {
            console.error(ex);

        }finally{
            setLoading(false);
        }
    }

    useEffect(() => {
        loadCates();
    }, []);

    
    useEffect(() => {
        loadRecruits();
    }, []);

    return (
        <View style={MyStyles.container}>
            <Text style={MyStyles.subject}>DANH MỤC CÔNG VIỆC</Text>

            <View style={MyStyles.row}>
                {categories.map(c => <Chip style={MyStyles.margin} icon="label" key={c.id}> {c.name} </Chip>)}
            </View>

            <View>
                {/* la kieu True thi cai vong tron nay chay kh thi kh chaychay */}
                {loading && <ActivityIndicator />}
            </View>
            
        </View>
    );
}

export default Home;