
import UIKit
import MapKit
import CoreLocation
import FirebaseDatabase


class MapViewController: UIViewController, CLLocationManagerDelegate {
    var latref: DatabaseReference?
    var longref: DatabaseReference?
    var phoneref: DatabaseReference?
    var usernameref: DatabaseReference?
    var latitude: String?
    var longitude: String?
    var locationManager = CLLocationManager()
    var counter: Int = 1
    
    var receivedata = [Int]()
    var receiveref: DatabaseReference?
    var dataBaseHandle: DatabaseHandle?
    
    @IBOutlet weak var mapView: MKMapView!
    
    @IBOutlet weak var StatusLabel: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        latref = Database.database().reference()
        longref = Database.database().reference()
        phoneref = Database.database().reference()
        usernameref = Database.database().reference()
        receiveref = Database.database().reference()
    
        
        dataBaseHandle = receiveref?.child("danger").observe(.childAdded, with: { (snapshot) in
            
            let post = snapshot.value as? Int
            
            if let actualPost = post {

                self.receivedata.append(actualPost)
                
                if(actualPost == 1){
                    self.StatusLabel.text = "CURRENT STATUS: SAFE ZONE"
                }
                if(actualPost == 0){
                     self.StatusLabel.text = "CURRENT STATUS: DANGER ZONE"
                }
            }
        })
        
      
        mapView.register(MKMarkerAnnotationView.self, forAnnotationViewWithReuseIdentifier: MKMapViewDefaultAnnotationViewReuseIdentifier)
        
        self.locationManager.requestWhenInUseAuthorization()
        
        if CLLocationManager.locationServicesEnabled(){
            locationManager.delegate = self
            locationManager.desiredAccuracy = kCLLocationAccuracyNearestTenMeters
            locationManager.startUpdatingLocation()
        }
        
        createAnnotations(locations: annotationLocations)
    }
    
  
    @IBAction func addPost(_ sender: Any) {
        latref?.child("User1").child("Latitude").setValue(latitude)
        latref?.child("User1").child("Longitude").setValue(longitude)
        latref?.child("User1").child("Phone Number").setValue("4342347862")
        latref?.child("User1").child("Username").setValue("Brian")
        latref?.child("User1").child("Timestamp").setValue("12:00:00")
    }
    
    
    @IBAction func refresh(_ sender: Any) {
//        latref?.child("Update").child("\(counter).child("Latitude").setValue(latitude)
//        latref?.child("Update").child(counter).child("Longitude").setValue(longitude)
//
//        counter = counter + 1
        
        
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        let locValue: CLLocationCoordinate2D = manager.location!.coordinate
        latitude = "\(locValue.latitude)"
        longitude = "\(locValue.longitude)"
        //locValue.latitude locValue.longitude
//        let userLocation = locations.last
//        let viewRegion = MKCoordinateRegion(center: (userLocation?.coordinate)!, latitudinalMeters: 600,longitudinalMeters: 600)
//        self.mapView.setRegion(viewRegion, animated: true)
    }
    
    
    let annotationLocations = [
        ["title": "Student Center", "latitude": 42.359050, "longitude": -71.094760],

    ]
    func createAnnotations(locations: [[String: Any]]) {
                for location in locations{
                    let annotations = MKPointAnnotation()
                    annotations.title = location["title"] as? String
                    annotations.coordinate = CLLocationCoordinate2D(latitude: location["latitude"] as! CLLocationDegrees, longitude: location["longitude"] as! CLLocationDegrees)
                    mapView.addAnnotation(annotations)
        }
        
        var region: MKCoordinateRegion{
            let span = MKCoordinateSpan(latitudeDelta: 0.005, longitudeDelta: 0.005)
            let chapelCoordinate = CLLocationCoordinate2D(latitude: 42.359050, longitude: -71.094760)
            return MKCoordinateRegion(center: chapelCoordinate, span: span)
        }
        mapView.setRegion(region, animated: true)
        
    }
}
