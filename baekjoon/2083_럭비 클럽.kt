fun main() {

    while (true) {
        // 파싱
        val (name, age, weight) = readLine()!!.split(" ")
        
        // 탈출
        if (name == "#") {
            break
        }
        
        // 결과출력
        when {
            (age.toInt() > 17) -> println("${name} Senior")
            (weight.toInt() >= 80) -> println("${name} Senior")
            else -> println("${name} Junior")
        }
    }
}
