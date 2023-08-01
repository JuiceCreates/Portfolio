public class TrafficLightEnum {
  enum TrafficLight {
    RED(20), GREEN(30), YELLOW(5);

    TrafficLight(int duration) {
      this.duration = duration;
    }

    private int duration;

    public int getDuration() {
      return duration;
    }
  }

  public static void main(String args[]){
    TrafficLight[] trafficLights = TrafficLight.values();
    for(TrafficLight trafficLight: trafficLights){
      System.out.println(trafficLight.name()+" duration is "+trafficLight.getDuration()+".");
    }
  }
}
