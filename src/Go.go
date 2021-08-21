func (id *IdentityId) checkCode() bool {
    weights := []int{7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2}
    codes   := []string{"1", "0", "X", "9", "8", "7", "6", "5", "4", "3", "2"}
    sum := 0
    for i := 0; i < 17; i++ {
        n, _ := strconv.Atoi(string(id.Code[i]))    
        sum += n * weight[i]        
    }
    
    m := sum % 11
    
    return code[m] == id.Code[17:]
}