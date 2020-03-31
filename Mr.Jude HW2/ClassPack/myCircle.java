package ClassPack;

public class myCircle {
    private myPoint center = new myPoint(0,0);
    private int radius = 1;

    public myCircle(){
        this.center = new myPoint(0,0);
        this.radius = 1;
    }
    public myCircle(int x, int y, int radius){
        this.setCenter(new myPoint(x,y));
        this.setRadius(radius);
    }
    public myCircle(myPoint center, int radius){
        this.setCenter(center);
        this.setRadius(radius);
    }

    public int getRadius() {
        return radius;
    }

    public void setRadius(int radius) {
        this.radius = radius;
    }

    public myPoint getCenter() {
        return center;
    }

    public void setCenter(myPoint center) {
        this.center = center;
    }
    public int getCenterX(){
        return center.getX();
    }
    public void setCenterX(int x){
        this.center.setX(x);
    }
    public int getCenterY(){
        return center.getY();
    }
    public void setCenterY(int y){
        this.center.setY(y);
    }
    public void setCenterXY(int x, int y){
        this.center.setXY(x,y);
    }

    @Override
    public String toString() {
        return "myCircle{" + "radius=" + radius + " center=" + center + '}';
    }
    public double getArea(){
        return Math.PI*radius*radius;
    }
    public double getCircum(){
        return Math.PI*radius*2;
    }
    public double distance(myCircle another){
        return center.distance(another.center);
    }
    //the getXY method isnt included
}
