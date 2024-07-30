import { useRef, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Offcanvas from 'react-bootstrap/Offcanvas';
import DatePicker from "react-datepicker";

import "react-datepicker/dist/react-datepicker.css";

export default function EditCard( { data, setData, goal } ){
  const [show, setShow] = useState(false);
  const [startDate, setStartDate] = useState( goal.date );

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const titleRef = useRef( null );
  const bodyRef = useRef( null );

  const ButtonClickHandler = () => {
    const newArray = [];
    data.map( card => {
        if( card.key !== goal.key ){
            newArray.push( card )
        }
    });
    const title = titleRef.current.value;
    const body = bodyRef.current.value;
    setData([ { key: goal.key, title: title, body: body, date:startDate}, ...newArray])
  }

  const markAsCompleteHandler = () => {
    const newArray = [];
    data.map( card => {
        if( card.key !== goal.key ){
            newArray.push( card )
        }
    });
    setData([...newArray])
  }

  return (
    <>
      <Button variant="primary m-2" onClick={handleShow}>
        Edit
      </Button>
      <Button variant="primary m-2" onClick={markAsCompleteHandler}>
        Mark As Complete
      </Button>

      <Offcanvas className="bg-dark text-white" show={show} onHide={handleClose}>
        <Offcanvas.Header closeButton>
          <Offcanvas.Title>Edit Goals</Offcanvas.Title>
        </Offcanvas.Header>
        <Offcanvas.Body>
          <div className='p-3'>
            <p className='lead'>Title: </p>
            <input ref={titleRef} type='text' className='form-control' defaultValue={ goal.title } ></input>
          </div>
          <div className='p-3'>
            <p className='lead'>Date: </p>
            <DatePicker selected={startDate} onChange={(date) => setStartDate(date)} />
          </div>
          <div className='p-3'>
            <p className='lead'>Body: </p>
            <textarea ref={bodyRef} type='text' rows={5} className='form-control' defaultValue={ goal.body } ></textarea>
          </div>
          <div className='p-3'>
            <button className='btn btn-primary' onClick={ ButtonClickHandler }> Save Changes</button>
          </div>
        </Offcanvas.Body>
      </Offcanvas>
    </>
  );
}