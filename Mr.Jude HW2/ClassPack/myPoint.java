package ClassPack;

public class myPoint {
    private int x = 0;
    private int y = 0;

    public myPoint(){
        this.x = 0;
        this.y = 0;
    }
    public myPoint(int x, int y){
        this.setX(x);
        this.setY(y);
    }
    public int getX() {
        return x;
    }
    public void setX(int x) {
        this.x = x;
    }
    public int getY() {
        return y;
    }
    public void setY(int y) {
        this.y = y;
    }
    /*public int[] getXY(){ there's an error here
        int[] XY;
        String out = "";
        XY[0] = x;
        XY[1] = y;
        for (int i=0;i<XY.length;i++){
            if (XY[i] == null){
                break;
            }
            else{
                out += XY.toString() + ", ";
            }
        }
        return out;
    }*/
    public void setXY(int x, int y){
        this.x = x;
        this.y = y;
    }
    @Override
    public String toString() {
        return "(" + x + ", " + y + ")";
    }
    public double distance(int x, int y){
        int xdis = this.x - x;
        int ydis = this.y - y;
        return Math.sqrt(xdis*xdis + ydis*ydis);
    }
    public double distance(myPoint another){
        int xdis2 = this.x - another.x;
        int ydis2 = this.y - another.y;
        return Math.sqrt(xdis2*xdis2 + ydis2*ydis2);
    }
    public double distance(){
        return 0;
    }
}
