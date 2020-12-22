class Card extends Payment{
    constructor(id, date, cvv){
        super(id)
        this.date = date;
        this.cvv = cvv;
    }
}