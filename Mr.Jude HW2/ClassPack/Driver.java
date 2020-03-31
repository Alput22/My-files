package ClassPack;

public class Driver {
    public static void main(String[] args){
        myPoint p1 = new myPoint(3,4);
        myPoint p2 = new myPoint(8,9);
        myPoint p3 = new myPoint(6,5);
        System.out.println(p1);

        myCircle c1 = new myCircle(p1,2);
        System.out.println(c1);

        myTriangle t1 = new myTriangle(p1, p2, p3);
        System.out.println(t1);

    }
}
