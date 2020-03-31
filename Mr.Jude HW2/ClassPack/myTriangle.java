package ClassPack;

public class myTriangle {
    private myPoint v1 = new myPoint();
    private myPoint v2 = new myPoint();
    private myPoint v3 = new myPoint();

    public myTriangle(int x1, int y1,int x2, int y2,int x3, int y3){
        this.v1 = new myPoint(x1,y1);
        this.v2 = new myPoint(x2,y2);
        this.v3 = new myPoint(x3,y3);
    }
    public myTriangle(myPoint v1, myPoint v2,myPoint v3){
        this.v1 = v1;
        this.v2 = v2;
        this.v3 = v3;
    }

    @Override
    public String toString() {
        return "myTriangle{" + "v1=" + v1 + ", v2=" + v2 + ", v3=" + v3 + '}';
    }
    public double getPerim(){
        return v1.distance(v2) + v2.distance(v3) + v1.distance(v3);
    }
    public String getType(){
        if (v1.distance(v2) == v2.distance(v3) && v1.distance(v2) == v1.distance(v3) && v2.distance(v3) == v1.distance(v3)){
            return "equilateral";
        }
        if (v1.distance(v2) == v2.distance(v3) || v1.distance(v2) == v1.distance(v3) || v2.distance(v3) == v1.distance(v3)){
            return "isosceles";
        }
        else{
            return "scalene";
        }
    }
}
