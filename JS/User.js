class User extends Account{
    constructor(name, document, paymentType){
        super(name, document)
        this.paymentType = paymentType
    }
    
}